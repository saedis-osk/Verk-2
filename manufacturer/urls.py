
from django.urls import path
from . import views
    # http://localhost:8000/manufactures
urlpatterns = [
    path('', views.index, name="index"),
]
