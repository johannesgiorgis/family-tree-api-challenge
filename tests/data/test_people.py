from family_tree.data.people import Person


def test_new_user():
    """
    GIVEN a Person model
    WHEN a new Person is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    new_person = Person(first_name="John", last_name="Smith", email="john.smith@test.com")

    assert new_person.first_name == "John"
    assert new_person.last_name == "Smith"
    assert new_person.email == "john.smith@test.com"
