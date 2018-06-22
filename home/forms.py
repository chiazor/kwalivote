from django import forms
from .models import home
from django.forms import ModelForm
from django.db import models


class LoginForm(forms.Form):
	username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control'}))
	password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

	class Meta:
		model = home
		fields = "__all__"
