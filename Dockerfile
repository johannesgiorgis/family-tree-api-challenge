FROM python:3.6.10-slim-buster

RUN pip install --upgrade pip \
    && pip install pipenv

ENV FTA=/family-tree-api
WORKDIR ${FTA}

COPY Pipfile* ./

RUN pipenv install --deploy --ignore-pipfile
COPY family_tree family_tree/
COPY manage.py .

CMD ["pipenv", "run", "python", "manage.py"]