"""
People Model & Schema
---------------------

Contains both the Person and ParentChildRelationship models
"""

# from datetime import datetime

from family_tree.config import db, ma

# from family_tree.data.modelbase import BaseModel
from . import BaseModel


class Person(BaseModel):

    first_name: str = db.Column(db.String, nullable=False)
    last_name: str = db.Column(db.String, nullable=False)

    phone_number: str = db.Column(db.String, nullable=True)
    email: str = db.Column(db.String, nullable=True)
    address: str = db.Column(db.String, nullable=True)
    birth_date: str = db.Column(db.Date, nullable=True)

    # # relationships: parents
    # parents = db.relationship("Person", secondary="parentchildrelation")
    parents = db.relationship(
        "Person",
        secondary="progeny",
        primaryjoin="Person.id==progeny.c.parent_id",
        secondaryjoin="Person.id==progeny.c.child_id",
        lazy="joined",
    )
    # # relationships: children
    # children = orm.relation("Person", secondary="ParentChildRelationship")

    def __repr__(self):
        return f"<Person {self.id}>"


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person


# class Progeny(BaseModel):

#     parent_id: int = db.Column(db.Integer, db.ForeignKey("person.id"))
#     child_id: int = db.Column(db.Integer, db.ForeignKey("person.id"))

#     def __repr__(self):
#         return f"<Parent {self.parent_id} -> Child {self.child_id}>"


# class ParentChildRelationSchema(ma.ModelSchema):
#     class Meta:
#         model = ParentChildRelation
