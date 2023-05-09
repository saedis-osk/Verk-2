from django import forms
from django.forms import ModelForm, widgets
from menu.models import Pizza, ToppingsCandy, ToppingsFruit, ToppingsSauces


class PizzaCreateForm(forms.ModelForm):
    toppings_candy = forms.ModelMultipleChoiceField(
        queryset=ToppingsCandy.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    toppings_fruit = forms.ModelMultipleChoiceField(
        queryset=ToppingsFruit.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    toppings_sauces = forms.ModelMultipleChoiceField(
        queryset=ToppingsSauces.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Pizza
        exclude = ['id']
        fields = ('name', 'description', 'image')

class PizzaUpdateForm(forms.ModelForm):
    toppings_candy = forms.ModelMultipleChoiceField(
        queryset=ToppingsCandy.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    toppings_fruit = forms.ModelMultipleChoiceField(
        queryset=ToppingsFruit.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    toppings_sauces = forms.ModelMultipleChoiceField(
        queryset=ToppingsSauces.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Pizza
        exclude = ['id']
        fields = ('name', 'description', 'image')



# class PizzaUpdateForm(ModelForm):
#     class Meta:
#         model = Pizza
#         exclude = ['id']
#         widgets = {
#             'name': widgets.TextInput(attrs={'class': 'form-control'}),
#             'description': widgets.TextInput(attrs={'class': 'form-control'}),
#             'category': widgets.TextInput(attrs={'class': 'form-control'}),
#             'ingredient': widgets.TextInput(attrs={'class': 'form-control'}),
#             'size': widgets.TextInput(attrs={'class': 'form-control'}),
#             'toppings': widgets.TextInput(attrs={'class': 'form-control'}),
#             'price': widgets.NumberInput(attrs={'class': 'form-control'})
#         }
#
#
# class PizzaCreateForm(ModelForm):
#     image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     class Meta:
#         model = Pizza
#         exclude = ['id']
#         widgets = {
#             'name': widgets.TextInput(attrs={'class': 'form-control'}),
#             'description': widgets.TextInput(attrs={'class': 'form-control'}),
#             'category': widgets.TextInput(attrs={'class': 'form-control'}),
#             'ingredient': widgets.TextInput(attrs={'class': 'form-control'}),
#             'size': widgets.TextInput(attrs={'class': 'form-control'}),
#             'toppings': widgets.TextInput(attrs={'class': 'form-control'}),
#             'toppings': widgets.TextInput(attrs={'class': 'form-control'}),
#             'price': widgets.NumberInput(attrs={'class': 'form-control'})
#         }
