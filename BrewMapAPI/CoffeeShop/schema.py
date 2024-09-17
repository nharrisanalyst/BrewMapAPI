from typing import List
from ninja import Schema
from CoffeeShop.models import Shop

class AddressScheme(Schema):
    city:str
    address_1:str
    address_2:str = None
    state:str
    zip_code:str


class MenuScheme(Schema):
    name:str
    price:float
    reporter:str


class PointSchema(Schema):
    lat:float
    long:float


class CoffeeShopScheme(Schema):
    name:str
    address:AddressScheme
    phone_number:int
    menu_list:list[MenuScheme]
    miles:float
    point:PointSchema
    

