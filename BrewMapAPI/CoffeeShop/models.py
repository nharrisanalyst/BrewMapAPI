from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from Generic.models import OpeningHours, UsLocation
from phonenumber_field.modelfields import PhoneNumberField
from Menu.models import Menu
from CoffeeShop.utils.LatLong import LatLong
from django.contrib import admin
from django.contrib.gis import admin as admin_gis
# Create your models here.



class Shop(gis_models.Model):
    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(region="US", blank=True)
    openingHours = models.ManyToManyField(OpeningHours)
    address = models.OneToOneField(UsLocation, on_delete=models.CASCADE)
    menu = models.OneToOneField(Menu, on_delete=models.CASCADE)
    lat = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    long = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)

    ##point is the actual point on  globe where this store is 
    point = gis_models.PointField(
        blank=True,
        null=True,
        spatial_index=True
    )

    @property
    def average_rating(self):
        return  self.rating_set.all().aggregate(models.Avg('rate'))['rate__avg']

    def save(self, **kwargs):
        
        latLong = LatLong(self.name, self.address)
        latLong.setLatLong()
        if latLong.long and latLong.lat:
            self.lat = latLong.lat
            self.long = latLong.long
        
        if self.long and self.lat:
            self.point = Point(
                float(self.long),
                float(self.lat),
                srid=4326
            )
        else:
            self.point = None
        
        super().save(**kwargs)


   

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop , on_delete=models.CASCADE)
    rate  = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])


class ShopAdmin(admin_gis.GISModelAdmin):
     


    
admin.site.register(Shop,ShopAdmin)