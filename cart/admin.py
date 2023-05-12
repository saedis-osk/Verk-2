from django.contrib import admin

from cart.models import Payment
from cart.cart import Cart

# Register your models here.

admin.site.register(Payment)
admin.register(Cart)