from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from menu.models import Pizza, Drink, Toppings
from menu.forms.forms import PizzaCreateForm, PizzaUpdateForm
from itertools import groupby

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



def get_pizza_by_id(request, id):
    return render(request, 'menu/pizza_details.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })


from itertools import groupby


def create_pizza(request):
    toppings_by_type = {}  # Initialize toppings_by_type here

    if request.method == 'POST':
        form = PizzaCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza_image = request.FILES.get('image')
            if pizza_image:
                pizza.image = pizza_image
            pizza.save()

            toppings_ids = request.POST.getlist('toppings')
            toppings = Toppings.objects.filter(id__in=toppings_ids)
            toppings_by_type = {k: list(g) for k, g in groupby(toppings, lambda t: t.type)}
            for topping in toppings:
                print(topping)
                topping_image = request.FILES.get('topping_image_{}'.format(topping.id))
                if topping_image:
                    topping.image = topping_image
                    topping.save()
                pizza.toppings.add(topping)

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

def menu(request):
    pizzas = Pizza.objects.all()
    drinks = Drink.objects.all()
    context = {'pizzas': pizzas, 'drinks': drinks}
    return render(request, 'menu/menu.html', context)



