def regiment_product(item) -> dict:
    """Regiment an entity from a database how it should look."""
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item["description"],
        "options": item["options"],
    }


def regiment_products_entity(entity) -> list:
    """Regiment a lot of entities from a database how it should look."""
    return [regiment_product(item) for item in entity]
