from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
'''
for p in self.cart.keys():
    self.cart[str(p)]['product'] = Product.objects.get(pk=p)
    
Þarf að geta flett upp hvaða id/key og fá viðeigandi object, Pizza, drink eða offer.
Dict key verður product id/key
Value verður how many
'''
class Item(models.Model): #PRODUCT ER PARENT AF PIZZA, DRINKS OG OFFERS
    quantity = models.IntegerField()
    class Meta:
        app_label = 'cart.item'

# Create your models here.
class Payment(models.Model):
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))

    class Meta:
        app_label = 'cart.card'
    def __str__(self):
        return f'{self.cc_number} - {self.cc_expiry}'



