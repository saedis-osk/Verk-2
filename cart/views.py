from django.shortcuts import render, get_object_or_404
from cart.models import Cart
# Create your views here.

def index(request):
    context = {'cart': Cart.objects.all().order_by('user')}#a ad rada fra user eda cart??
    return render(request, 'cart/index.html', context)

def get_cart_by_id(request, id):
    return render(request, cart, 'cart/cart_details.html', {
        'cart': get_object_or_404(Cart, pk=id)
    })

def create_cart(request):
    if request.method == 'POST':
        print(1)
    else:
        form = CartCreateForm()
    return render(request, 'cart/create_cart.html', {
        'from': form
    })
