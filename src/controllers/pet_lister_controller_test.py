from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Dudu", type="cat", id=7),
            PetsTable(name="Sofy", type="dog", id=4),
        ]

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name":"Dudu","id":7},
                {"name":"Sofy","id":4}
            ]
        }
    }

    assert response == expected_response
