"""
People Module
"""

from datetime import datetime

from flask import abort, make_response

from family_tree.config import db
from family_tree.data.people import Person, PersonSchema


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# ################### /people #################################


def read_all() -> dict:
    """
    This function responds to a request for /api/people
    with the complete list of people

    :return:    json string of list of people
    """
    people = Person.query.order_by(Person.last_name).all()

    # Serialize teh data for the response
    person_schema = PersonSchema(many=True)
    return person_schema.dump(people)


def create(person: dict):
    """
    This function responds to a request for /api/people

    :param person:  person to create
    :return:        201 on success, 406 on person exists
    """

    # Check for existing person
    existing_person = (
        Person.query.filter(Person.first_name == person["first_name"])
        .filter(Person.last_name == person["last_name"])
        .one_or_none()
    )

    if existing_person is None:

        person_schema = PersonSchema()
        new_person = person_schema.load(person, session=db.session)

        db.session.add(new_person)
        db.session.commit()

        data = person_schema.dump(new_person)

        return data, 201

    else:
        abort(409, f"Person '{person.get('first_name')} {person.get('last_name')}' already exists")


# ################### /people/<person_id> #################################


def read_one(person_id: int):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people

    :param person_id:   ID of person to find
    :return:            person matching person ID
    """

    person = Person.query.filter(Person.id == person_id).one_or_none()

    if person is not None:

        person_schema = PersonSchema()
        return person_schema.dump(person)

    else:
        abort(404, f"Person with ID '{person_id}' not found")


def update(person_id: int, person: dict):
    """
    This function updates an existing person in the people structure

    :param person_id:   ID of the person to update
    :param person:      person to update
    :return:            updated person structure
    """

    existing_person = Person.query.filter(Person.id == person_id).one_or_none()

    if existing_person is not None:

        person_schema = PersonSchema()
        update = person_schema.load(person, session=db.session)

        update.id = existing_person.id

        db.session.merge(update)
        db.session.commit()

        data = person_schema.dump(existing_person)
        return data, 200

    else:
        abort(404, f"Person with ID {person_id} not found")


def delete(person_id: int):
    """
    This function deletes a person from the people structure

    :param person_id:   ID of person to delete
    :return:            200 on successful delete, 404 if not found
    """

    person = Person.query.filter(Person.id == person_id).one_or_none()

    if person is not None:
        db.session.delete(person)
        db.session.commit()
        return make_response(f"Person with ID {person_id} successfully deleted")

    else:
        abort(404, f"Person with ID {person_id} not found")
