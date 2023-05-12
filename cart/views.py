from django.shortcuts import render, redirect, get_object_or_404
from menu.models import Pizza
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .cart import Cart
from django.template import RequestContext
from django.contrib.auth.models import User
from creditcards import types

def index(request):
    cart = Cart(request)
    context = {
        "cart":cart.cart
    }
    print(cart.cart)
    return render(request, 'cart/index.html', context)


def detect_card_type(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        card_type = types.get_type(card_number)
        if card_type is not None:
            return render(request, 'card_type.html', {'card_type': card_type})
        else:
            return render(request, 'card_type.html', {'error': 'Could not determine card type.'})
    else:
        return render(request, 'card_type_form.html')



def profile_view(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'user': user})


def confirmation(request):
    return render(request, 'cart/confirmation.html')


def checkout(request):
    return render(request, 'cart/checkout.html')


def information(request):
    return render(request, 'cart/information.html')

def successful(request):
    return render(request, 'cart/successful.html')

