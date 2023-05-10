from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from menu.models import Pizza, Drink, ToppingsCandy, ToppingsFruit, ToppingsSauces
from menu.forms.forms import PizzaCreateForm, PizzaUpdateForm

# Create your views here.


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        pizza = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.pizzaimage_set.first().image
        } for x in Pizza.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': pizza})

    context = {'pizza': Pizza.objects.all().order_by('name')}
    return render(request, 'menu/index.html', context)



def toppings_view(request):
    toppings_candy = ToppingsCandy.objects.all()
    toppings_fruit = ToppingsFruit.objects.all()
    toppings_sauces = ToppingsSauces.objects.all()
    return render(request, 'menu/pizza_details.html', {
        'toppings_candy': toppings_candy,
        'toppings_fruit': toppings_fruit,
        'toppings_sauces': toppings_sauces,
    })



def get_pizza_by_id(request, id):
    return render(request, 'menu/pizza_details.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })


def create_pizza(request):
    if request.method == 'POST':
        form = PizzaCreateForm(data=request.POST)
        if form.is_valid():
            pizza = form.save()
            pizza_image = PizzaImage(image=request.POST['image'], pizza=pizza)
            pizza_image.save()
            return redirect('pizza-index')
    else:
        form = PizzaCreateForm()
    return render(request, 'menu/create_pizza.html', {
        'form': form
    })


def delete_pizza(request, id):
    pizza = get_object_or_404(Pizza, pk=id)
    pizza.delete()
    return redirect('pizza-index')


def update_pizza(request, id):
    instance = get_object_or_404(Pizza, pk=id)
    if request.method == 'POST':
        form = PizzaUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('pizza_details', id=id)
    else:
        form = PizzaUpdateForm(instance=instance)
    return render(request, 'menu/update_pizza.html', {
        'form': form,
        'id': id
    })


def offers(request):
    return render(request, 'menu/offers.html')

def drinks(request):
    return render(request, 'menu/drinks.html')




