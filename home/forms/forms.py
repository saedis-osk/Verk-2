from django import forms
from django.forms import ModelForm, widgets
from home.models import PopularOffer

class OfferPopularCreateForm(ModelForm):
    image = forms.FileField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = PopularOffer
        exclude = ['id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }