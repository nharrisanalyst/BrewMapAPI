from django.apps import AppConfig
from ninja.orm import fields
from geojson_pydantic import Point 


class CoffeeshopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CoffeeShop'

    def ready(self) -> None:
        fields.TYPES.update({"PointField": Point})
        return super().ready()
