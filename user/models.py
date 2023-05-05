from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)



