from django.urls import path
from . import views
from .views import toppings_view


    # http://localhost:8000/manufactures
urlpatterns = [
    path('', views.index, name="menu-index"),
    path('<int:id>', views.get_pizza_by_id, name="pizza_details"),
    path('create_pizza', views.create_pizza, name="create_pizza"),
    path('delete_pizza/<int:id>', views.delete_pizza, name="delete_pizza"),
    path('update_pizza/<int:id>', views.update_pizza, name="update_pizza"),
    path('toppings/', toppings_view, name='toppings'),

]
