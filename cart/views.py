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


#def confirmation(request):
 #   return render(request, 'cart/confirmation.html')


def checkout(request):
    return render(request, 'cart/checkout.html')


def information(request):
    return render(request, 'cart/information.html')

def successful(request):
    return render(request, 'cart/successful.html')




def confirmation_view(request):
    if request.method == 'POST':
        # Assuming you have retrieved the form data and processed it
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        street = request.POST.get('street')
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        expiration = request.POST.get('expiration')
        cvc = request.POST.get('cvc')
        total = request.POST.get('total')

        context = {
            'email': email,
            'phone_number': phone_number,
            'city': city,
            'zip_code': zip_code,
            'street': street,
            'card_name': card_name,
            'card_number': card_number,
            'expiration': expiration,
            'cvc': cvc,
            'total': total
        }
        return render(request, 'cart/confirmation.html', context)

    # Handle cases when the view is accessed via GET request
    return render(request, 'cart/confirmation.html')


