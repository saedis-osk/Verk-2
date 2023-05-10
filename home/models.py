from django.db import models
from menu.models import Pizza, Drink
# Create your models here.


class PopularOffer(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='offer/', default='offer/default.png')

    def __str__(self):
        return self.name
