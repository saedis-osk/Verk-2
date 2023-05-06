# Generated by Django 4.2 on 2023-05-04 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('size', models.CharField(blank=True, max_length=255)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('ingredient', models.CharField(blank=True, max_length=255)),
                ('size', models.CharField(blank=True, max_length=255)),
                ('toppings', models.CharField(blank=True, max_length=255)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PizzaCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=9999)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.pizza')),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.pizzacategory'),
        ),
        migrations.CreateModel(
            name='DrinkImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=9999)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.drink')),
            ],
        ),
    ]
