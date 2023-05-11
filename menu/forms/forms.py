from django import forms
from django.forms import ModelForm, widgets
from menu.models import Pizza, Toppings, Drink, Offer


class PizzaUpdateForm(ModelForm):
    class Meta:
        model = Pizza
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.TextInput(attrs={'class': 'form-control'}),
            'ingredient': widgets.TextInput(attrs={'class': 'form-control'}),
            'toppings': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'})
        }


class PizzaCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Pizza
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.TextInput(attrs={'class': 'form-control'}),
            'ingredient': widgets.TextInput(attrs={'class': 'form-control'}),
            'toppings': widgets.TextInput(attrs={'class': 'form-control'}),
            'toppings': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'})
        }

class DrinkCreateForm(ModelForm):
    image = forms.FileField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Drink
        exclude = ['id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }

class OfferCreateForm(ModelForm):
    image = forms.FileField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Offer
        exclude = ['id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }