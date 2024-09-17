from typing import List
from ninja import Router
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from CoffeeShop.schema import CoffeeShopScheme
from CoffeeShop.models import Shop


router = Router()

@router.get('/hello')
def hello(request):
    return "hello world"

@router.get('/list', response = list[CoffeeShopScheme])
def list_coffee_shops(request,lat:float, long:float):
    distance_miles_to_search = 10
    pnt = Point(
                float(lat),
                float(long),
                srid=4326
            )
    shops_all = Shop.objects.all()
    print('this is all the shops',shops_all[0].point, pnt, lat, long)
    shops = Shop.objects.filter(point__distance_lte=(pnt, D(mi=distance_miles_to_search)))
    print('these are the shops',shops)
    return list(shops)



@router.get('/latlong')
def get_lat_long(request, lat:int, long:int):
    return f"latitude is {lat} and longitude is {long}"