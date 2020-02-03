from datetime import datetime
import sqlalchemy as sa
from flask_marshmallow import Marshmallow

from family_tree.data.modelbase import SqlAlchemyBase

ma = Marshmallow()


class Person(SqlAlchemyBase):

    __tablename__ = "people"

    id: int = sa.Column(sa.Integer, primary_key=True)

    first_name: str = sa.Column(sa.String, nullable=False)
    last_name: str = sa.Column(sa.String, nullable=False)

    phone_number: str = sa.Column(sa.String, nullable=True)
    email: str = sa.Column(sa.String, nullable=True)
    address: str = sa.Column(sa.String, nullable=True)
    birth_date: str = sa.Column(sa.Date, nullable=True)

    created_timestamp: datetime = sa.Column(sa.DateTime, default=datetime.utcnow)
    updated_timestamp: datetime = sa.Column(
        sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # relationships: parents
    # relationships: children

    def __repr__(self):
        return f"<Person {self.id}>"


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
