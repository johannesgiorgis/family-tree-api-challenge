from datetime import datetime
from typing import List, Optional

import family_tree.data.db_session as db_session
from family_tree.data.people import Person, PersonSchema


def get_initial_people() -> dict:
    """
    Initial People Data to serve with our API
    """
    return {
        "Farrell": {
            "first_name": "Doug",
            "last_name": "Farrell",
            "phone_number": "778-200-2005",
            "email": "doug.farrell@gmail.com",
            "address": "123 Lasne St",
            "birth_date": datetime.strptime("1980-08-24", "%Y-%m-%d"),
        },
        "Brockman": {
            "first_name": "Kent",
            "last_name": "Brockman",
            "phone_number": "778-200-1004",
            "email": "kent.brockman@hotmail.com",
            "address": "56 E 89th St",
            "birth_date": datetime.strptime("1984-02-07", "%Y-%m-%d"),
        },
        "Easter": {
            "first_name": "Bunny",
            "last_name": "Easter",
            "phone_number": "604-300-7821",
            "email": "bunny.easter@yahoo.com",
            "address": "34 Happy Joy St",
            "birth_date": datetime.strptime("2015-06-20", "%Y-%m-%d"),
        },
    }


# ################### /people #################################


def get_people() -> List[Person]:
    session = db_session.create_session()

    try:
        people = session.query(Person).all()

        person_schema = PersonSchema(many=True)

        return person_schema.dump(people)
    finally:
        session.close()


def find_person(person: dict) -> Optional[Person]:
    session = db_session.create_session()
    try:
        return (
            session.query(Person)
            .filter(Person.first_name == person["first_name"])
            .filter(Person.last_name == person["last_name"])
            .one_or_none()
        )
    finally:
        session.close()


def create_new_person(person: dict) -> Optional[dict]:

    if find_person(person):
        return None

    session = db_session.create_session()

    try:
        schema = PersonSchema()
        new_person = schema.load(person, session=session)

        session.add(new_person)
        session.commit()

        return schema.dump(new_person)

    finally:
        session.close()


# ################### /people/<person_id> #################################


def find_person_by_id(person_id: id) -> Optional[Person]:
    session = db_session.create_session()
    try:
        return session.query(Person).filter(Person.id == person_id).one_or_none()
    finally:
        session.close()


def get_person(person_id: int) -> Optional[dict]:

    existing_person = find_person_by_id(person_id)
    if not existing_person:
        return None

    person_schema = PersonSchema()
    return person_schema.dump(existing_person)


def update_person(person_id: int, person: dict) -> Optional[dict]:

    update_person = find_person_by_id(person_id)

    if not update_person:
        return None

    person_schema = PersonSchema()

    session = db_session.create_session()

    try:
        update = person_schema.load(person, session=session)

        # TO DO: Seems to not send the correct updated timestamp
        update.id = update_person.id
        update.created_date = update_person.created_date

        session.merge(update)
        session.commit()

        return person_schema.dump(update_person)

    finally:
        session.close()


def delete_person(person_id: int) -> bool:

    existing_person = find_person_by_id(person_id)

    if not existing_person:
        return False

    session = db_session.create_session()

    try:
        session.delete(existing_person)
        session.commit()

    finally:
        session.close()

    return True
