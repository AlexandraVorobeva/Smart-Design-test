from fastapi import APIRouter, Depends, Response, status
from ..db import db
from ..schemas.product import product_entity, products_entity
from bson import ObjectId, BSON
from ..models.product import Product
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/products")


@router.get('/all')
def find_all_products():
    all_products = db.product.find()
    return products_entity(all_products)


@router.get('/{product_id}')
def find_product_by_id(id):
    product = db.product.find_one({"_id": ObjectId(id)})
    return product_entity(product)

@router.get('/{product_name}')
def find_product_by_name(name: str):
    n = db.product.find_one({'name': name})
    return n


@router.post('/new')
def create_product(product: Product):
    new_product = dict(product)
    id = db.product.insert(new_product).inserted_id
    product = db.product.find_one({"_id": id})
    return product_entity(product)