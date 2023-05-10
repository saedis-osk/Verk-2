from django.forms import ModelForm, widgets
from django import forms
from cart.models import Cart
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

class PaymentForm(forms.Form):
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')


class CartCreateForm(ModelForm):
    class Meta:
        model = Cart
        exclude = ['id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'pizza': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'toppings': forms.TextInput(attrs={'class': 'form-control'}),
            'created_at': forms.DateInput(attrs={'class': 'form-control'}),
            'updated_at': forms.DateInput(attrs={'class': 'form-control'}),
        }


