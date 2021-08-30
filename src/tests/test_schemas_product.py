from src.schemas.product import regiment_product, regiment_products_entity


data = [
    {
        "_id": "61221765c8dc29d4a9ada364",
        "name": "John",
        "description": "boy",
        "options": {},
    },
    {
        "_id": "6122270ef9fa04e0488e318b",
        "name": "Joanna",
        "description": "girl",
        "options": {},
    },
]


def test_regiment_product(data):
    assert regiment_product(data[0]) == {
        "id": "61221765c8dc29d4a9ada364",
        "name": "John",
        "description": "boy",
        "options": {},
    }


def test_regiment_products_entity(data):
    assert regiment_products_entity(data) == [
        {
            "id": "61221765c8dc29d4a9ada364",
            "name": "John",
            "description": "boy",
            "options": {},
        },
        {
            "id": "6122270ef9fa04e0488e318b",
            "name": "Joanna",
            "description": "girl",
            "options": {},
        },
    ]
