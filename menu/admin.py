from django.contrib import admin
from menu.models import Pizza
from menu.models import Drink
from menu.models import Offer
from menu.models import ToppingsCandy
from menu.models import ToppingsFruit
from menu.models import ToppingsSauces
from menu.models import PizzaCategory

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Drink)
admin.site.register(Offer)
admin.site.register(ToppingsCandy)
admin.site.register(ToppingsFruit)
admin.site.register(ToppingsSauces)
admin.site.register(PizzaCategory)
