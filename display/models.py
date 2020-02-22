from django import forms
from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user.username}\'s Portfolio'


class Coin(models.Model):
    owner = models.ForeignKey(Portfolio, on_delete = models.CASCADE)
    name_of_coin = models.CharField(max_length = 100)
    amount_holding = models.DecimalField(default = 0, blank = True, max_digits = 20, decimal_places=10)

    def __str__(self):
        return self.name_of_coin
