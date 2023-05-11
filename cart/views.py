from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render
from creditcards import types

# Create your views here.

def index(request):
    return render(request, 'cart/index.html')


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