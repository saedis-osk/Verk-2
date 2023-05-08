from django.forms import ModelForm, widgets
from cart.models import Cart

 class CartCreateForm(ModelForm):
     class Meta:
         model = Cart
         exclude = ['id']
         widgets = {
            'name': widgets.TextInput(attrs={'class': form-control}),
            'pizza':widgets.TextInput(attrs={'class': form-control}),
            'quantity': widgets.NumberInput(attrs={'class': form-control}),
            'size': widgets.TextInput(attrs={'class': form-control}),
            'toppings': widgets.TextInput(attrs={'class': form-control}),
            'created_at':widgets.DateInput(attrs={'class': form-control}),
            'updated_at':widgets.DateInput(attrs={'class': form-control}),
         }

