from django.db import models

# Create your models here.

# class CandyCategory(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name


# class Candy(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255, blank=True)
#     category = models.ForeignKey(CandyCategory, on_delete=models.CASCADE)
#     price = models.FloatField()
#     on_sale = models.BooleanField()
#     manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name


# class CandyImage(models.Model):
#     image = models.CharField(max_length=9999)
#     candy = models.ForeignKey(Candy, on_delete=models.CASCADE)
#     logo = models.CharField(max_length=9999, blank=True)

    # def __str__(self):
    #     return self.image
