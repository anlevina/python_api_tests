from pydantic import BaseModel
from typing import List


class Usertype(BaseModel):
    usertype: str


class Category(BaseModel):
    usertype: Usertype
    category: str


class Product(BaseModel):
    id: int
    name: str
    price: str
    brand: str
    category: Category


class GetSearchProductResponse(BaseModel):
    responseCode: int
    products: List[Product]