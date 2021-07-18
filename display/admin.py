from django.contrib import admin

from .models import Coin, Portfolio

admin.site.register(Portfolio)
admin.site.register(Coin)
