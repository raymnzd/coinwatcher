from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from display import views as display_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", display_views.index, name="index-page"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="display/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="display/logout.html"),
        name="logout",
    ),
    path("register/", display_views.register, name="register"),
    path("coins/", include("display.urls")),
    path("portfolio/", display_views.portfolio, name="portfolio-page"),
]
