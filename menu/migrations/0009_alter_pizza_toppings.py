# Generated by Django 4.2 on 2023-05-09 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_pizza_category_alter_pizza_toppings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ForeignKey(default='test2', on_delete=django.db.models.deletion.CASCADE, to='menu.toppings'),
        ),
    ]
