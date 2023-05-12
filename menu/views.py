from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from menu.models import Pizza, Drink, Toppings, Offer, Category
from menu.forms.forms import PizzaCreateForm, PizzaUpdateForm, DrinkCreateForm, OfferCreateForm
from itertools import groupby
from cart.cart import Cart
# Create your views here.



def index(request):
    pizzas = Pizza.objects.all()

    sort_order = request.GET.get('sort')
    if sort_order == 'price':
        pizzas = pizzas.order_by('price')
    elif sort_order == 'alpha' or sort_order is None:
        pizzas = pizzas.order_by('name')

    if 'search_filter' in request.GET or sort_order:
        pizza_data = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.pizzaimage_set.first().image if x.pizzaimage_set.first() else None
        } for x in pizzas]
        return JsonResponse({'data': pizza_data})

    categories = Category.objects.all().values_list('id', 'name')

    # Retrieve the selected category filter
    category_filter = request.GET.get('category')
    if category_filter:
        pizzas = pizzas.filter(categories__id=int(category_filter))

    context = {'pizzas': pizzas, 'categories': categories, 'category_filter': category_filter}

    return render(request, 'menu/index.html', context)


def get_pizza_by_id(request, id):
    return render(request, 'menu/pizza_details.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })


def create_pizza(request):
    toppings_by_type = {}  # Initialize toppings_by_type here

    if request.method == 'POST':
        form = PizzaCreateForm(data=request.POST, files=request.FILES)
        print(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza_image = request.FILES.get('image')
            if pizza_image:
                pizza.image = pizza_image
            pizza.save()

            toppings_ids = request.POST.getlist('toppings')
            toppings = Toppings.objects.filter(id__in=toppings_ids).order_by('type')
            for topping in toppings:
                topping_image = request.FILES.get('topping_image_{}'.format(topping.id))
                if topping_image:
                    topping.image = topping_image
                    topping.save()
                pizza.toppings.add(topping)

            # Adding categories to pizza
            categories_names = request.POST.getlist('categories')
            categories = Category.objects.filter(name__in=categories_names)
            for category in categories:
                pizza.categories.add(category)

            pizza.save()  # Save pizza after adding categories

            toppings_by_type = {k: list(g) for k, g in groupby(toppings, lambda t: t.type)}
            context = {
                'pizza': pizza,
                'toppings_by_type': toppings_by_type,
            }
            cart = Cart(request)
            cart.add(pizza.id)
            cart.save()
            print(cart.cart)
            return render(request, 'menu/create_pizza.html', context)
    else:
        form = PizzaCreateForm()
        toppings = Toppings.objects.all()
        toppings_by_type = {k: list(g) for k, g in groupby(toppings, lambda t: t.type)}

    return render(request, 'menu/create_pizza.html', {
        'form': form,
        'toppings_by_type': toppings_by_type,
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



def drinks(request):
    if request.method == 'POST':
        form = DrinkCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            drink = form.save(commit=False)
            drink_image = request.FILES.get('image')
            if drink_image:
                drink.image = drink_image
            drink.save()
    drinks = Drink.objects.all()
    context = {'drinks': drinks}
    return render(request, 'menu/drinks.html', context)

def offers(request):
    if request.method == 'POST':
        form = OfferCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            offer = form.save(commit=False)
            offer_image = request.FILES.get('image')
            if offer_image:
                offer.image = offer_image
            offer.save()
    offers = Offer.objects.all()
    context = {'offers': offers}
    return render(request, 'menu/offers.html', context)

