from django.db import models

# Create your models here.


class PizzaCategory(models.Model):
    name = models.CharField(max_length=255)

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(PizzaCategory, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=255, blank=True)
    toppings = models.CharField(max_length=255, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

class PizzaImage(models.Model):
    image = models.CharField(max_length=9999)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=255, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name



class DrinkImage(models.Model):
    image = models.CharField(max_length=9999)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return self.image



