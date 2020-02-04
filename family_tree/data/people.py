"""
People Model & Schema
---------------------
"""

from datetime import datetime

from family_tree.config import db, ma


class Person(db.Model):

    __tablename__ = "people"

    id: int = db.Column(db.Integer, primary_key=True)

    first_name: str = db.Column(db.String, nullable=False)
    last_name: str = db.Column(db.String, nullable=False)

    phone_number: str = db.Column(db.String, nullable=True)
    email: str = db.Column(db.String, nullable=True)
    address: str = db.Column(db.String, nullable=True)
    birth_date: str = db.Column(db.Date, nullable=True)

    created_timestamp: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    updated_timestamp: datetime = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # # relationships: parents
    # parents = db.relationship("Person", secondary="parentchildrelation")
    # parents = db.relationship(
    #     "Person",
    #     secondary="parentchildrelation",
    #     primaryjoin="Person.id==parentchildrelation.c.parent_id",
    #     secondaryjoin="Person.id==parentchildrelation.c.child_id",
    #     lazy="joined",
    # )
    # # relationships: children
    # children = orm.relation("Person", secondary="ParentChildRelationship")

    def __repr__(self):
        return f"<Person {self.id}>"


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
