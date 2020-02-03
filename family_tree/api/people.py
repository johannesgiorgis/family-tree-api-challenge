"""
People Module
"""

from datetime import datetime

from flask import abort, make_response

# from family_tree.data.people import Person, PersonSchema
import family_tree.services.people_service as people_service


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# ################### /people #################################


def read_all():
    """
    This function responds to a request for /api/people
    with the complete list of people

    :return:    json string of list of people
    """
    return people_service.get_people()


def create(person: dict):
    """
    This function responds to a request for /api/people

    :param person:  person to create
    :return:        201 on success, 406 on person exists
    """

    # Check for existing person
    new_person = people_service.create_new_person(person)

    if not new_person:
        abort(409, f"Person '{person.get('first_name')} {person.get('last_name')}' already exists")

    else:
        return new_person, 201


# ################### /people/<person_id> #################################


def read_one(person_id: int):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people

    :param person_id:   ID of person to find
    :return:            person matching person ID
    """
    person = people_service.get_person(person_id)

    if not person:

        abort(404, f"Person with ID '{person_id}' not found")

    else:
        return person


def update(person_id: int, person: dict):
    """
    This function updates an existing person in the people structure

    :param person_id:   ID of the person to update
    :param person:      person to update
    :return:            updated person structure
    """

    updated_person = people_service.update_person(person_id, person)

    if not updated_person:
        abort(404, f"Person with ID {person_id} not found")

    else:
        return updated_person, 200


def delete(person_id: int):
    """
    This function deletes a person from the people structure

    :param person_id:   ID of person to delete
    :return:            200 on successful delete, 404 if not found
    """

    if people_service.delete_person(person_id):
        return make_response(f"Person {person_id} successfully deleted")

    else:
        abort(404, f"Person with ID {person_id} not found")
