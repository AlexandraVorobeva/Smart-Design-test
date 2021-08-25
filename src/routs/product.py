from fastapi import APIRouter
from ..db import db
from ..schemas.product import regiment_product, regiment_products_entity
from bson import ObjectId
from ..models.product import Product

router = APIRouter(prefix="/products")


@router.get("/all")
def find_all_products():
    """Return list of all products from the database."""
    all_products = db.product.find()
    return regiment_products_entity(all_products)


@router.get("/{product_id}")
def find_product_by_id(id):
    """This function finds a product and info about it in the database by id."""
    product = db.product.find_one({"_id": ObjectId(id)})
    return regiment_product(product)


@router.get("/all/{product_parameter}")
def filter_products_by_parameter(parameter, value=None):
    """
    Finds products by parameters and value. In case you using only parameter
    all products will be sorted in alphabetical order.

    Parameter must be "name" or "options".

    Value: any
    """
    products = []
    if not value:
        for product in db.product.find().sort(parameter):
            products.append(product)
    if parameter == "name":
        for product in db.product.find({"name": str(value)}):
            products.append(product)
    else:
        # нескольуих вариантов
        for product in db.product.find({"options": {parameter: value}}):
            products.append(product)
    return regiment_products_entity(products)


@router.post("/new")
def create_product(product: Product):
    """Creates a new product in the database"""
    new_product = dict(product)
    id = db.product.insert(new_product)
    product = db.product.find_one({"_id": id})
    return regiment_product(product)
