
from django.urls import path
from . import views
    # http://localhost:8000/candies
urlpatterns = [
    path('', views.index, name="candy-index"),
]
