from ninja import Router
from CoffeeShop.schema import CoffeeShopOut

router = Router()

@router.get('/hello')
def hello(request):
    return "hello world"

@router.get('/list')
def list_coffee_shops(request,lat:float, long:float ):
    return "hello world"



@router.get('/latlong')
def get_lat_long(request, lat:int, long:int):
    return f"latitude is {lat} and longitude is {long}"