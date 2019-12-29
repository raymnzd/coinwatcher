from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name = 'index-page'),
    path('login/', auth_views.LoginView.as_view(template_name = 'display/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'display/logout.html'), name = 'logout'),
    path('coins/', views.listcoins, name = 'list-page'),
    path('coin/<cryptoname>', views.coin, name = 'crypto-page'),
    path('testpage/', views.test, name = 'test-page'),

]
