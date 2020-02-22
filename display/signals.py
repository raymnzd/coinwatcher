from .models import Portfolio
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_portfolio(sender, instance, created, **kwargs):
    if created:
        Portfolio.objects.create(user=instance)
        print("Portfolio created!")
