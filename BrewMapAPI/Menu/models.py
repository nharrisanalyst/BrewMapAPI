from django.db import models

# Create your models here.



class LatteMenuItem(models.Model):
    name = 'Latte'
    price = models.DecimalField(max_digits=4, decimal_places=2)

class BlackCoffeeMenuItem(models.Model):
    name='Black Coffee'
    price = models.DecimalField(max_digits=4, decimal_places=2)

class Menu(models.Model):
    latte = LatteMenuItem()
    black = BlackCoffeeMenuItem()
    


class MenuItem(models.Model):
    name = models.CharField(max_length = 25)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    menu = models.ForeignKey(Menu , on_delete=models.CASCADE)