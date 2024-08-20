from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from Generic.models import UsLocation, OpeningHours
from phonenumber_field.modelfields import PhoneNumberField
from Menu.models import Menu
from CoffeeShop.utils.LatLong import LatLong

# Create your models here.



class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = UsLocation()
    phone_number = PhoneNumberField(blank=True)
    openingHours = OpeningHours()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    lat = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, default='0')
    long = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, default='0')

    @property
    def average_rating(self):
        return  self.rating_set.all().aggregate(models.Avg('rate'))['rate__avg']

    def save(self, **kwargs):
        super().save(**kwargs)
        latLong = LatLong(self.name, self.address)
        latLong.setLatLong()
        if latLong.long and latLong.lat:
            self.lat = latLong.lat
            self.long = latLong.long
            self.save()
        


   

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop , on_delete=models.CASCADE)
    rate  = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    