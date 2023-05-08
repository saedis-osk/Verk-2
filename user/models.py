from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Account(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True)
    mail = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='users/', default='users/default.png')

# class CardInfo(models.Model):
#     card_number
#     cvv =
#     date =

    # -username
    # -password

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)

