from django.contrib import admin
from cart.models import Cart
from cart.models import Payment


# Register your models here.
admin.site.register(Cart)
admin.site.register(Payment)

