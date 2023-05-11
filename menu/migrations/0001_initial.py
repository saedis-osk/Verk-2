# Generated by Django 4.2 on 2023-05-10 23:39

from django.db import migrations, models
import django.db.models.deletion
import menu.models


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
                ('price', models.FloatField(default=0.0)),
                ('image', models.ImageField(default='drink/default.png', upload_to='drink/')),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(default='/toppings/default.png', upload_to='toppings/')),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('category', models.CharField(blank=True, max_length=10, null=True)),
                ('ingredient', models.CharField(blank=True, max_length=255)),
                ('size', models.CharField(blank=True, max_length=255)),
                ('price', models.FloatField(default=0.0)),
                ('image', models.ImageField(default='/pizza/default.png', upload_to='pizza/')),
                ('toppings', models.ForeignKey(default=menu.models.Toppings, on_delete=django.db.models.deletion.CASCADE, to='menu.toppings')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(default='offer/default.png', upload_to='offer/')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.drink')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.pizza')),
            ],
        ),
    ]
