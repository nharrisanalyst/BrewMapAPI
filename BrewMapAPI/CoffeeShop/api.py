from ninja import Router
from CoffeeShop.schema import CoffeeShopOut

router = Router()

@router.get('/hello')
def hello(request):
    return "hello world"

@router.get('/list')
def list_coffee_shops(request,lat:float, long:float ):
    return "hello world"