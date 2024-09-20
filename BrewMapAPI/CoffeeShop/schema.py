
from ninja.orm import fields
from ninja import Schema
from typing import Optional
from CoffeeShop.models import Shop
from phonenumber_field.phonenumber import PhoneNumber


class AddressSchema(Schema):
    city:str
    address_1:str
    address_2:str = None
    state:str
    zip_code:str
    


class MenuItemSchema(Schema):
    name:str
    price:float
    reporter:str
    


class MenuSchema(Schema):
    latte:MenuItemSchema
    black:MenuItemSchema
    menuItems:Optional[list[MenuItemSchema]] = None
    

class PointSchema(Schema):
    lat:float
    long:float
    


class CoffeeShopSchema(Schema):
    name:str
    address:AddressSchema
    phone_number:str
    menu_list:list[MenuItemSchema]
    miles:float
    point:PointSchema
    class Config:
        arbitrary_types_allowed=True

class CoffeeShopReturnSchema(Schema):
    shops:list[CoffeeShopSchema]
    class Config:
        arbitrary_types_allowed=True

    
    

