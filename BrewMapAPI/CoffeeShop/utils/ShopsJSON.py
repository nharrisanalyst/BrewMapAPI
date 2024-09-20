from CoffeeShop.models import Shop
from CoffeeShop.schema import CoffeeShopSchema
from Menu.models import MenuItem, BlackCoffeeMenuItem, LatteMenuItem

def Menu_to_JSON(menu_item: MenuItem | BlackCoffeeMenuItem | LatteMenuItem) ->dict:
    return {
        "name":menu_item.name,
        "price":float(menu_item.price),
        "reporter":menu_item.reporter
    }
    


def Shop_to_JOSN(shop:Shop):
    menuItems = []
    if shop.menu.menuItems is not None:
        for item in menuItems:
            menuItems.append(Menu_to_JSON(item))
    
    return {
        "name":shop.name,
        "address":{
            "city":shop.address.city,
            "address_1":shop.address.address_1,
            "address_2":shop.address.address_2,
            "state":shop.address.state,
            "zip_code":shop.address.zip_code,
        },
        "phone_number":str(shop.phone_number.national_number),
        "menu_list":[
            Menu_to_JSON(shop.menu.latte), Menu_to_JSON(shop.menu.black), *menuItems
        ],
        "miles":shop.distance.mi,
        "point":{
            "lat":shop.point.coords[0],
            "long":shop.point.coords[1]
        }
    }


    