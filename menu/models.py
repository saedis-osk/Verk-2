from django.db import models
from cart.models import Item


# Create your models here.

class Toppings(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='toppings/', default='/toppings/default.png')
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.name



class Pizza(models.Model):
    FRUITY = 'Fruity'
    VEGAN = 'Vegan'
    POPULAR = 'Popular'

    CATEGORY_CHOICES = [
        (FRUITY, 'Fruity'),
        (VEGAN, 'Vegan'),
        (POPULAR, 'Popular'),
    ]

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, null=True, blank=True)
    toppings = models.ManyToManyField(Toppings)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='pizza/', default='/pizza/default.png')

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.name



class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='drink/', default='drink/default.png')

    def __str__(self):
        return self.name



class Offer(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='offer/', default='offer/default.png')

    def __str__(self):
        return self.name