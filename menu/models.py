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
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='pizza/', default='pizza/default.png')



    def __str__(self):
        return self.name

class PizzaImage(models.Model):
    image = models.ImageField(max_length=9999)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class Toppings(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name





class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=255, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='drink/', default='drink/default.png')

    def __str__(self):
        return self.name



class DrinkImage(models.Model):
    image = models.ImageField(max_length=9999)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class Offer(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


# Offer
# -id
# -name
# -prices
# -pizzas
# -descriptions
# -images
# -drinks


