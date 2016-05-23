from django import forms
from .models import chef

class chef_form(forms.Form):
	chef_code = forms.IntegerField()
	chef_name = forms.CharField()
	chef_age  = forms.IntegerField()
	chef_area = forms.CharField()

class chefFormSet(forms.ModelForm):
	class Meta:
		model = chef
		fields = '__all__'