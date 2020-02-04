"""
Relationship Model
------------------

To start with a simple approach, I decided on
a Parent - Child Relationship

I kept encountering the following error while running `python manage.py`
and was unable to find a solution:

    sqlalchemy.exc.InvalidRequestError: When initializing mapper mapped class,
    expression failed to locate a name ("name 'parentchildrelation' is not defined").
    If this is a class name, consider adding this relationship() to
    the <class 'family_tree.data.people.Person'> class after both dependent classes
    have been defined.

Went as far as copying the model/ from https://github.com/alysivji/flask-family-tree-api
which I verified was able to run successfully via `python manage.py`

Our pipenv files had differences and I had encountered library version mismatch
issues before which led to the same code not working. Going through SQLAlchemy's
tutorials and documents didn't yield any answers.

Given the time limits imposed for this challenge, I will leave it here with the
intention of figuring this out.
"""

# from datetime import datetime

# # import sqlalchemy as sa
# # from family_tree.data.modelbase import SqlAlchemyBase

# from family_tree.config import db, ma


# class ParentChildRelation(db.Model):

#     __tablename__ = "parentchild"

#     id: int = db.Column(db.Integer, primary_key=True)

#     parent_id: int = db.Column(db.Integer, db.ForeignKey("people.id"))
#     child_id: int = db.Column(db.Integer, db.ForeignKey("people.id"))

#     created_timestamp: datetime = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_timestamp: datetime = db.Column(
#         db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
#     )

#     def __repr__(self):
#         return f"<Parent {self.parent_id} -> Child {self.child_id}>"


# class ParentChildRelationSchema(ma.ModelSchema):
#     class Meta:
#         model = ParentChildRelation
