from django.db import models
from django.contrib import admin

# Create your models here.



class LatteMenuItem(models.Model):
    name = models.CharField(max_length=30, default='Latte')
    price = models.DecimalField(max_digits=4, decimal_places=2)

class BlackCoffeeMenuItem(models.Model):
    name=models.CharField(max_length=30, default='Black Coffee')
    price = models.DecimalField(max_digits=4, decimal_places=2)

class MenuItem(models.Model):
    name = models.CharField(max_length = 25)
    price = models.DecimalField(max_digits=4, decimal_places=2)

class Menu(models.Model):
    latte = models.OneToOneField(LatteMenuItem, on_delete=models.CASCADE)
    black = models.OneToOneField(BlackCoffeeMenuItem, on_delete=models.CASCADE)
    menuItems = models.ForeignKey(MenuItem, on_delete=models.CASCADE, blank=True, null=True)

admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(LatteMenuItem)
admin.site.register(BlackCoffeeMenuItem)