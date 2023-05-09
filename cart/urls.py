from django.urls import path
from . import views

    # http://localhost:8000/manufactures

urlpatterns = [
    path('', views.index, name="cart-index"),
    path('<int:id>', views.get_cart_by_id, name="cart_details"),
    path('create_cart', views.create_cart, name="create_cart")
]
