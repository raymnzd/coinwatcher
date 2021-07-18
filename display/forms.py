from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Coin, Portfolio


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class AddCryptoForm(forms.Form):
    add_amount = forms.DecimalField()


class RemoveCryptoForm(forms.Form):
    remove_amount = forms.DecimalField()
