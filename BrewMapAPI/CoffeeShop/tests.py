from django.test import TestCase
from ninja.testing import TestClient
from CoffeeShop.utils.LatLong import LatLong
from CoffeeShop.api import router
from Generic.models import UsLocation 

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

class LAtLongUtilTest(TestCase):
    def test_lat_long_util(self):
        name = "Shady Coffee & Tea"
        address = UsLocation(city="Roseville", state="CA", address_1="325 Douglas Blvd", zip_code="95678")
        latLong = LatLong(name,address)
        latLong.setLatLong()
        self.assertAlmostEqual(latLong.lat, '38.744030')
        self.assertAlmostEqual(latLong.long, '-121.287331')