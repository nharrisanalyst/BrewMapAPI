# Generated by Django 5.1 on 2024-08-21 01:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeShop', '0003_alter_shop_address_alter_shop_openinghours'),
        ('Generic', '0002_alter_openinghours_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='openingHours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Generic.openinghours'),
        ),
    ]
