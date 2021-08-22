def product_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item["description"],
        "options": item["options"]
    }


def products_entity(entity) -> list:
    return [product_entity(item) for item in entity]
