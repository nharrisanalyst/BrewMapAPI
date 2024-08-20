from geopy.geocoders import Nominatim

class LatLong:
    def __init__(self, name:str, address:str):
        self.name = name
        self.address = address
        self.loc = self.name + ", " + self.address
        self.geolocator =  Nominatim(user_agent="my_request")
        self.lat = None
        self.long = None

    def setLatLong(self):
        self.location = self.geolocator.geocode(self.loc)
        self.lat = self.location.latitude
        self.long = self.location.longitude


