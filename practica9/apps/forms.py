from django import forms
from django.contrib.auth.forms import UserCreationForm

class User_form(UserCreationForm):
	mail=forms.CharField(max_length=24)
	phone=forms.IntegerField()
