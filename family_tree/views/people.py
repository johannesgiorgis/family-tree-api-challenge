"""
People Module
"""

from datetime import datetime

from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "person_id": 1,
        "first_name": "Doug",
        "last_name": "Farrell",
        "phone_number": "",
        "email": "",
        "address": "",
        "birth_date": "",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "person_id": 2,
        "first_name": "Kent",
        "last_name": "Brockman",
        "phone_number": "",
        "email": "",
        "address": "",
        "birth_date": "",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "person_id": 3,
        "first_name": "Bunny",
        "last_name": "Easter",
        "phone_number": "",
        "email": "",
        "address": "",
        "birth_date": "",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    """
    This function responds to a request for /api/people
    with the complete list of people

    :return:    json string of list of people
    """
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def read_one(last_name: str):
    """
    This function responds to a request for /api/people/{last_name}
    with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name
    """
    if last_name in PEOPLE:
        person = PEOPLE.get(last_name)
    else:
        abort(404, f"Person with last name {last_name} not found")

    return person


def create(person: dict):
    """
    This function responds to a request for /api/people/

    :param person:  person to create
    :return:        201 on success, 406 on person exists
    """
    first_name = person.get("first_name", None)
    last_name = person.get("last_name", None)

    if last_name not in PEOPLE and last_name is not None:
        person_id = len(PEOPLE) + 1
        dynamic_data = {"person_id": person_id, "timestamp": get_timestamp()}
        PEOPLE[last_name] = {**person, **dynamic_data}

        return PEOPLE[last_name], 201

    else:
        abort(406, f"Person with last name {last_name} already exists")


def update(last_name: str, person: dict):
    """
    This function updates an existing person in the people structure

    :param last_name:   Last name of the person to update
    :param person:      person to update
    :return:            updated person structure
    """
    if last_name in PEOPLE:
        PEOPLE[last_name]["first_name"] = person.get("first_name")
        PEOPLE[last_name]["timestamp"] = get_timestamp()

        return PEOPLE[last_name]

    else:
        abort(404, f"Person with last name {last_name} not found")


def delete(last_name: str):
    """
    This function deletes a person from the people structure

    :param last_name:   last name of person to delete
    :return:            200 on successful delete, 404 if not found
    """
    if last_name in PEOPLE:
        del PEOPLE[last_name]
        return make_response(f"{last_name} successfully deleted")
    else:
        abort(404, f"Person with last name {last_name} not found")
