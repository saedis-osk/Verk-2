# Generated by Django 4.2 on 2023-05-12 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_remove_pizza_ingredient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toppings',
            options={'ordering': ['type']},
        ),
    ]
