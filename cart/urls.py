from django.urls import path
from . import views

from .views import confirmation
from .views import checkout
from .views import information
from .views import successful



urlpatterns = [
    path('', views.index, name="cart-index"),

    path('confirmation/', views.confirmation, name='confirmation'),
    path('successful/', views.successful, name='successful'),
    path('information/', views.information, name='information'),
    path('checkout/', views.checkout, name='checkout'),
#    path('<int:id>', views.get_cart_by_id, name="cart_details"),
#    path('create_cart', views.create_cart, name="create_cart")
]

    #path('confirmation/', views.confirmation, name='confirmation'),
    #path('checkout/', views.checkout, name='checkout'),
    #path('<int:id>', views.get_cart_by_id, name="cart_details"),
    #path('create_cart', views.create_cart, name="create_cart"),
    #path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    #path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    #path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    #path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    #path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    #path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

