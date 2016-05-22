from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class User_form(UserCreationForm):
	email = forms.CharField(max_length=99)
