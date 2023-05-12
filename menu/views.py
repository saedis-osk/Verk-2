from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from menu.models import Pizza, Drink, Toppings, Offer, Category
from menu.forms.forms import PizzaCreateForm, PizzaUpdateForm, DrinkCreateForm, OfferCreateForm
from itertools import groupby
from cart.cart import Cart
from cart.forms.forms import CartAddForm
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
        #print(request.POST)
        #print(form.is_valid())
        #print(form.errors)
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

            toppings_by_type = {k: list(g) for k, g in groupby(toppings, lambda t: t.type)}
            context = {
                'pizza': pizza,
                'toppings_by_type': toppings_by_type,
            }
            return render(request, 'menu/create_pizza.html', context)
    else:
        form = PizzaCreateForm()
        toppings = Toppings.objects.all()
        toppings_by_type = {k: list(g) for k, g in groupby(toppings, lambda t: t.type)}

    return render(request, 'menu/create_pizza.html', {
        'form': form,
        'toppings_by_type': toppings_by_type,
    })


def add_pizza(request):
    toppings_by_type = {}  # Initialize toppings_by_type here
    pizza_name = ""  # Initialize pizza_name variable
    pizza_description = ""  # Initialize pizza_description variable

    if request.method == 'POST':
        form = CartAddForm(data=request.POST, files=request.FILES)
        print(form.is_valid())
        if form.is_valid():
            pizza = form.save(commit=False)
            toppings_ids = request.POST.getlist('toppings')
            toppings = Toppings.objects.filter(id__in=toppings_ids)
            for topping in toppings:
                topping_image = request.FILES.get('topping_image_{}'.format(topping.id))
                if topping_image:
                    topping.image = topping_image
                else:
                    topping.image = None# 404 needed here

            toppings_by_type = {k: list(g) for k, g in groupby(toppings, lambda t: t.type)}
            context = {
                'selected_pizza': {
                    'name': pizza.name,
                    'description': pizza.description,
                    'price': pizza.price
                },
                'toppings_by_type': toppings_by_type,
            }

            # Add the pizza details to the session cart
            cart = Cart(request)
            cart.add(context)
            cart.save()
            print("ADDED TO CART")
            print(f"Context selected : {context}")

            # Assign the pizza name and description to the variables


            return redirect('cart-index')  # Redirect to the cart page
    else:
        form = CartAddForm()
        toppings = Toppings.objects.all()
        toppings_by_type = {k: list(g) for k, g in groupby(toppings, lambda t: t.type)}

    return render(request, 'menu/create_pizza.html', {
        'form': form,
        'toppings_by_type': toppings_by_type,
        'pizza_name': pizza_name,
        'pizza_description': pizza_description,  # Pass the pizza description to the template
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



from django.http import JsonResponse
from django.shortcuts import render

def drinks(request):
    drinks = Drink.objects.all()

    sort_order = request.GET.get('sort')
    if sort_order == 'price':
        drinks = drinks.order_by('price')
    elif sort_order == 'alpha' or sort_order is None:
        drinks = drinks.order_by('name')

    if 'search_filter' in request.GET or sort_order:
        drink_data = []
        for drink in drinks:
            first_image = drink.image.url if drink.image else None
            drink_data.append({
                'id': drink.id,
                'name': drink.name,
                'description': drink.description,
                'firstImage': first_image,
            })
        return render(request, 'menu/drinks.html', {'drinks': drinks})

    if request.method == 'POST':
        form = DrinkCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            drink = form.save(commit=False)
            drink_image = request.FILES.get('image')
            if drink_image:
                drink.image = drink_image
            drink.save()
    context = {'drinks': drinks}
    return render(request, 'menu/drinks.html', context)



# def get_pizza_by_id(request, id):
#     return render(request, 'menu/pizza_details.html', {
#         'pizza': get_object_or_404(Pizza, pk=id)
#     })
def drink_detail(request, drink_id):
    drink = get_object_or_404(Drink, id=drink_id)
    return render(request, 'menus/drink_detail.html', {'drink': drink})



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

