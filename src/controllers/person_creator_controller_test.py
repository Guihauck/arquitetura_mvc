import pytest
from .person_creator_controller import PeopleCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass

def test_create():
    person_info = {
        "first_name": "Guilherme",
        "last_name": "Hauck",
        "age": 26,
        "pet_id": 123
    }

    controller = PeopleCreatorController(MockPeopleRepository())
    response = controller.create(person_info)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_error():
    person_info = {
        "first_name": "Guilherme123",
        "last_name": "Hauck",
        "age": 26,
        "pet_id": 123
    }

    controller = PeopleCreatorController(MockPeopleRepository())

    with pytest.raises(Exception):
        controller.create(person_info)
