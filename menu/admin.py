from django.contrib import admin
from menu.models import Pizza
from menu.models import Drink
from menu.models import Offer
from menu.models import Toppings


# Register your models here.
admin.site.register(Pizza)
admin.site.register(Drink)
admin.site.register(Offer)
admin.site.register(Toppings)

