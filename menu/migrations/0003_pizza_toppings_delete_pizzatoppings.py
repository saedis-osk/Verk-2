# Generated by Django 4.2 on 2023-05-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_pizza_toppings_pizzatoppings'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='menu.toppings'),
        ),
        migrations.DeleteModel(
            name='PizzaToppings',
        ),
    ]