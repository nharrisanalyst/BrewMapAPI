from ninja import NinjaAPI

api = NinjaAPI()
@api.get("/hello")
def hello(request):
    return "Hello world"


api.add_router("/shops/", "CoffeeShop.api.router")