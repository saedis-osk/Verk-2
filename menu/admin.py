from django.contrib import admin
from menu.models import Pizza, Drink, Offer, Toppings


# PizzaToppings
# class PizzaToppingsInline(admin.TabularInline):  # or admin.StackedInline if you prefer
#     model = PizzaToppings
#     extra = 1  # defines the number of extra forms displayed
#
#
# class PizzaAdmin(admin.ModelAdmin):
#     inlines = [PizzaToppingsInline]


# Register your models here.
admin.site.register(Pizza)
admin.site.register(Drink)
admin.site.register(Offer)
admin.site.register(Toppings)
# admin.site.register(PizzaToppings)

