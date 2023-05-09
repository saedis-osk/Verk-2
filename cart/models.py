from django.db import models
from menu.models import Pizza
from user.models import User
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Payment(models.Model):
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))

    def __str__(self):
        return f'{self.cc_number} - {self.cc_expiry}'



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=10)
    toppings = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} x {self.size} {self.pizza.name} ({self.toppings})'





