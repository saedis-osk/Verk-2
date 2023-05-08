from django.shortcuts import render, get_object_or_404
from cart.models import Cart
from django.contrib.auth.models import User
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
        form = CartCreateForm(data=request.POST)
        if form.is_valid():
            cart = form.save()
    else:
        form = CartCreateForm()
    return render(request, 'cart/create_cart.html', {
        'from': form
    })

def profile_view(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'user': user})