from geopy.geocoders import Nominatim, options
from Generic.models import UsLocation
import ssl
import certifi 


ctx = ssl.create_default_context(cafile=certifi.where())
options.default_ssl_context = ctx

class LatLong:
    def __init__(self, name:str, address:UsLocation):
        self.name = name
        self.address = address
        
        ## self.loc = self.name + ", " + self.address
        address_2 = f" {self.address.address_2}" or ""
        if self.address.address_1 and self.address.city and self.address.state and self.address.zip_code:
            self.full_address:str = f"{self.address.address_1}{address_2}, {self.address.city}, {self.address.state}, {self.address.zip_code}"
        else:
            return ValueError("address does not include all parts")
        
        self.geolocator =  Nominatim(user_agent="my_request", scheme='http')
        self.lat = None
        self.long = None

    def setLatLong(self):
        
        self.location = self.geolocator.geocode(self.full_address)
        self.lat = self.location.latitude
        self.long = self.location.longitude


