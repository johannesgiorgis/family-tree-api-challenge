"""
Build database with People data
"""

from datetime import datetime
from pathlib import Path

from family_tree.config import db, sqlite_path
from family_tree.data.people import Person

# from family_tree.data.relationship import ParentChildRelation

PEOPLE = [
    {
        "first_name": "Papa",
        "last_name": "Hawke",
        "phone_number": "+1-778-200-2005",
        "email": "papa@hawk.com",
        "address": "123 Lasne St",
        "birth_date": datetime.strptime("1950-08-24", "%Y-%m-%d"),
    },
    {
        "first_name": "Leandra",
        "last_name": "Hawke",
        "phone_number": "+1-778-200-1004",
        "email": "leandra@hawke.com",
        "address": "123 Lasne St",
        "birth_date": datetime.strptime("1954-02-07", "%Y-%m-%d"),
    },
    {
        "first_name": "Declan",
        "last_name": "Hawke",
        "phone_number": "+1-604-300-7821",
        "email": "declan@hawke.com",
        "address": "123 Lasne St",
        "birth_date": datetime.strptime("1980-06-20", "%Y-%m-%d"),
    },
    {
        "first_name": "Bethany",
        "last_name": "Hawke",
        "phone_number": "+1-604-300-7821",
        "email": "bethany@hawke.com",
        "address": "123 Lasne St",
        "birth_date": datetime.strptime("1982-06-20", "%Y-%m-%d"),
    },
    {
        "first_name": "Carver",
        "last_name": "Hawke",
        "phone_number": "+1-604-300-7821",
        "email": "carver@hawke.com",
        "address": "123 Lasne St",
        "birth_date": datetime.strptime("1985-06-20", "%Y-%m-%d"),
    },
]

# DB_FILE =


def main():
    delete_db()
    init_db()
    insert_initial_data()


def delete_db():
    """
    Delete database file it exists currently
    """
    db_file = Path(sqlite_path)  # .parent.absolute().joinpath("family_tree/db/family.sqlite")

    if db_file.exists():
        db_file.unlink()


def init_db():
    # db_file = str(Path(__file__).parent.absolute().joinpath("family_tree/db/family.sqlite"))
    # db_session.global_init(sqlite_path)
    db.create_all()


def insert_initial_data():
    # session = db_session.create_session()

    # Iterate over the PEOPLE structure and populate the database
    # people = people_service.get_initial_people()
    for person in PEOPLE:
        p = Person(**person)
        db.session.add(p)

    db.session.commit()


if __name__ == "__main__":
    main()
