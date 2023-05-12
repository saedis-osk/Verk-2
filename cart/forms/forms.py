from django import forms
from django.forms import ModelForm, widgets
from menu.models import Pizza


class CartAddForm(ModelForm):
    image = forms.CharField(required=False,widget=forms.TextInput( attrs={'class': 'form-control'}))
    class Meta:
        model = Pizza
        exclude = ['id', 'price', 'name', 'toppings']
        widgets = {
            #'name': widgets.TextInput(attrs={'class': 'form-control'}),
            #'description': widgets.TextInput(attrs={'class': 'form-control'}),
            #'category': widgets.TextInput(attrs={'class': 'form-control'}),
            #'ingredient': widgets.TextInput(attrs={'class': 'form-control'}),
            'toppings': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
        }