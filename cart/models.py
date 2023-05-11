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



