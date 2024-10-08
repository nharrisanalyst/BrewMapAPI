# Generated by Django 5.1 on 2024-08-20 18:09

import localflavor.us.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=128, verbose_name='address')),
                ('address_2', models.CharField(blank=True, max_length=128, verbose_name="address cont'd")),
                ('city', models.CharField(default='Zanesville', max_length=64, verbose_name='city')),
                ('state', localflavor.us.models.USStateField(default='OH', max_length=2, verbose_name='state')),
                ('zip_code', models.CharField(default='43701', max_length=5, verbose_name='zip code')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
            ],
            options={
                'ordering': ('weekday', 'from_hour'),
                'unique_together': {('weekday', 'from_hour', 'to_hour')},
            },
        ),
    ]
