from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('homes/', views.popular_offers, name="home-index"),
    path('popular_offers/', views.popular_offers, name="home-popular-offers"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
