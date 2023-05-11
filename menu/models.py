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
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=10, null=True, blank=True)
    toppings = models.ManyToManyField(Toppings)
    ingredient = models.CharField(max_length=255, blank=True)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='pizza/', default='/pizza/default.png')


    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='drink/', default='drink/default.png')

    def __str__(self):
        return self.name


# class PizzaToppings(models.Model):
#     pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
#     topping = models.ForeignKey(Toppings, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.pizza


class Offer(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='offer/', default='offer/default.png')

    def __str__(self):
        return self.name