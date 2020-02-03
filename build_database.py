"""
Build database with People data
"""

from pathlib import Path

import family_tree.data.db_session as db_session
import family_tree.services.people_service as people_service
from family_tree.data.people import Person


def main():
    delete_db()
    init_db()
    insert_initial_data()


def delete_db():
    """
    Delete database file it exists currently
    """
    db_file = Path(__file__).parent.absolute().joinpath("family_tree/db/family.sqlite")

    if db_file.exists():
        db_file.unlink()


def init_db():
    db_file = str(Path(__file__).parent.absolute().joinpath("family_tree/db/family.sqlite"))
    db_session.global_init(db_file)


def insert_initial_data():
    session = db_session.create_session()

    # Iterate over the PEOPLE structure and populate the database
    people = people_service.get_initial_people()
    for person in people:
        p = Person(**people[person])
        session.add(p)

    session.commit()


if __name__ == "__main__":
    main()
