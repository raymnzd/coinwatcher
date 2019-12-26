from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home-page'),
    path('home/<cryptoname>', views.test2, name = 'home-crypto'),
    path('testpage/', views.test, name = 'test-page'),

]
