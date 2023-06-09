from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="menu-index"),
    path('<int:id>', views.get_pizza_by_id, name="pizza_details"),
    path('create_pizza', views.create_pizza, name="create_pizza"),
    path('delete_pizza/<int:id>', views.delete_pizza, name="delete_pizza"),
    path('update_pizza/<int:id>', views.update_pizza, name="update_pizza"),
    path('drinks/', views.drinks, name='drinks'),
    path('offers/', views.offers, name='offers'),
    path('update_pizza/<int:id>', views.update_pizza, name="update_pizza"),
    path('create_pizza/<int:id>', views.add_pizza, name="add_pizza"),
    path('add_pizza/<int:id>', views.add_pizza, name="add_pizza_id"),
    path('drink_detail/<int:drink_id>/', views.drink_detail, name='drink_detail'),
    path('add_drink/<int:id>', views.add_drink, name='add_drink')
]
