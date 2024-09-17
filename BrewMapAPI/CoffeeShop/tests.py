import os
from django.test import TestCase
import json
from ninja.testing import TestClient
from CoffeeShop.utils.LatLong import LatLong
from CoffeeShop.api import router
from Generic.models import UsLocation 
from Generic.models import OpeningHours
from Menu.models import LatteMenuItem, BlackCoffeeMenuItem, Menu 
from CoffeeShop.models import Shop

test_data_json = "CoffeeShop/test/testing_data.json"
test_open_json = "CoffeeShop/test/test_open_data.json"
test_response_json = "CoffeeShop/test/test_response.json"

# Create your tests here.
class HelloTest(TestCase):
    def test_hello(self):
        client = TestClient(router)
        response = client.get("/hello")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,  "hello world")


class LatLongTest(TestCase):
    def test_get_lat_long(self):
        client = TestClient(router)
        response = client.get("/latlong?lat=1&long=1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "latitude is 1 and longitude is 1")

class LatLongUtilTest(TestCase):
    def test_lat_long_util(self):
        name = "Shady Coffee & Tea"
        address = UsLocation(city="Roseville", state="CA", address_1="325 Douglas Blvd", zip_code="95678")
        latLong = LatLong(name,address)
        latLong.setLatLong()
        decimalPlace = 2
        self.assertAlmostEqual(latLong.lat, 38.744030, decimalPlace)
        self.assertAlmostEqual(latLong.long, -121.287331,decimalPlace)


class LatLongGetTest(TestCase):
    def setUp(self):
        with open(test_data_json) as json_data:
            data = json.load(json_data)
        with open(test_open_json) as json_data:
            data_open = json.load(json_data)
        openingHours_list =[]
        ## data for days of the week 
        print(data_open, 'this is a day')
        for day in data_open['data']:
            openingHours = OpeningHours(weekday=day["weekday"], from_hour=day["from_hour"], to_hour=day["to_hour"])
            openingHours.save()
            openingHours_list.append(openingHours)
        ## data for coffee shops
        for shop in data['data']:
            menu_data = shop['menu_list']
            for item in menu_data:
                if item['name'] == 'latte':
                    latte = LatteMenuItem(price = item['price'])
                    latte.save()
                else:
                    black_coffee = BlackCoffeeMenuItem(price = item['price'])
                    black_coffee.save()
            menu = Menu(latte = latte, black= black_coffee)
            menu.save()
            address = UsLocation(city=shop['address']['city'], state=shop['address']['state'], address_1=shop['address']['address_1'], zip_code=shop['address']['zip_code'])
            address.save()
            phone_number = shop['phone_number']
            shop_model= Shop(name=shop['name'], phone_number= phone_number, menu=menu, address= address)
            shop_model.save()
            shop_model.openingHours.add(*openingHours_list)
            
        
        

            
        
    def test_lat_long_get(self):
        ##getting test json data 
        with open(test_response_json) as json_data:
            response_test_data = json.load(json_data)
        self.client = TestClient(router)

        latitude = 38.73200589100485
        longitude = -121.2983564875914
        response = self.client.get(f"/list?lat={latitude}&long={longitude}")
        print(self)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), response_test_data)



