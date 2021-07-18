from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.listcoins, name="list-page"),
    path("<cryptoname>", views.coin, name="crypto-page"),
    path("testpage/", views.test, name="test-page"),
]
