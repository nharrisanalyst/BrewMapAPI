from typing import List
from ninja import Router
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from CoffeeShop.schema import CoffeeShopReturnSchema
from CoffeeShop.models import Shop
from CoffeeShop.utils.ShopsJSON import Shop_to_JOSN


router = Router()

@router.get('/hello')
def hello(request):
    return "hello world"

@router.get('/list', response = CoffeeShopReturnSchema)
def list_coffee_shops(request,lat:float, long:float):
    distance_miles_to_search = 10
    pnt = Point(
                float(lat),
                float(long),
                srid=4326
            )
    shops_all = Shop.objects.all()
    shops = Shop.objects.annotate(distance=Distance('point',pnt)).filter(point__distance_lte=(pnt, D(mi=distance_miles_to_search)))
    ShopsJSON = []
    for shop in shops:
        ShopsJSON.append(Shop_to_JOSN(shop))
    return 200, {"shops":ShopsJSON}



@router.get('/latlong')
def get_lat_long(request, lat:int, long:int):
    return f"latitude is {lat} and longitude is {long}"