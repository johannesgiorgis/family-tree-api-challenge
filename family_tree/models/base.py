"""
Base Model
----------
"""

from datetime import datetime

from sqlalchemy.ext.declarative import declared_attr

from family_tree.config import db


class BaseModel(db.Model):
    __abstract__ = True

    id: int = db.Column(db.Integer, primary_key=True)
    created_timestamp: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    date_modified: datetime = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # def patch(self, data: dict):
    #     for key, value in data.items():
    #         setattr(self, key, value)
