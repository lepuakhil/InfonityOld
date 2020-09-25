from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'first_name', 'last_name']


# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'profile_pic', 'address1', 'address2',
                  'city', 'state', 'pin']
