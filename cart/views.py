from django.shortcuts import render, redirect
from menu.models import Pizza
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .cart import Cart
from django.template import RequestContext

def index(request):
    cart = Cart(request)
    context = {
        "cart":cart
    }
    return render(request, 'cart/index.html', context)