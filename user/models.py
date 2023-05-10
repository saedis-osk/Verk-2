from django.db import models
from django.contrib.auth.models import User
# Create your models here.


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
    name = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)

