from django.urls import path
from . import views
from .views import confirmation
from .views import checkout

    # http://localhost:8000/manufactures

urlpatterns = [
    path('', views.index, name="cart-index"),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('checkout/', views.checkout, name='checkout'),
    path('<int:id>', views.get_cart_by_id, name="cart_details"),
    path('create_cart', views.create_cart, name="create_cart")
]
