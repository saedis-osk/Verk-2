# Generated by Django 4.2 on 2023-05-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_toppings_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='menu.toppings'),
        ),
    ]
