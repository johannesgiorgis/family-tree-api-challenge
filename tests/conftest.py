"""
Test Configuration
------------------


"""
import pytest

import sys
import os

# ensure pytest runs from project root directory
container_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, container_folder)

from family_tree.app import create_app
import family_tree.data.db_session as db_session


@pytest.fixture(scope="session")
def app():
    """
    """
    flask_app = create_app()
    flask_app.app.config["TESTING"] = True

    with flask_app.app.app_context():
        yield flask_app


@pytest.fixture(scope="session")
def client(app):
    yield app.app.test_client()


@pytest.fixture(scope="session")
def db(app):

    print(dir(db_session))
    db_session.app = app

    db_session.create_all()

    yield db_session

    db_session.drop_all()


# @pytest.fixture(scope="session")
# def db(app):
#     """Session-wide test database."""
#     _db.app = app
#     _db.create_all()
#     yield _db

#     _db.drop_all()


@pytest.fixture(scope="function")
def session(db):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()
    options = dict(bind=connection, binds={})

    session = db.create_scoped_session(options=options)
    db.session = session
    yield session

    transaction.rollback()
    connection.close()
    session.remove()
