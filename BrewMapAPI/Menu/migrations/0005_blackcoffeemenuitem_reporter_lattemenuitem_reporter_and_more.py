# Generated by Django 5.1 on 2024-08-29 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0004_alter_menu_menuitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='blackcoffeemenuitem',
            name='reporter',
            field=models.CharField(default='brewmapdata', max_length=25),
        ),
        migrations.AddField(
            model_name='lattemenuitem',
            name='reporter',
            field=models.CharField(default='brewmapdata', max_length=25),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='reporter',
            field=models.CharField(default='brewmapdata', max_length=25),
        ),
    ]
