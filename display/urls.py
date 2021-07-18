from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.listcoins, name="list-page"),
    path("<cryptoname>", views.coin, name="crypto-page"),
    path("testpage/", views.test, name="test-page"),
]
