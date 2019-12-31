from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Portfolio'



# class Coin(models.Model):
#     name_of_coin = models.CharField(max_length = 100)
#     amount_holding = models.CharField(max_length = 100)

    # def __str__(self):
        # return f'{self.name_of_coin}
