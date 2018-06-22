from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# from .models import home
# from django.forms import ModelForm
# from django.db import models


# class LoginForm(forms.Form):
# 	username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control'}))
# 	password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

# 	class Meta:
# 		model = home
# 		fields = "__all__"

User = get_user_model()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None


    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    # save user method
    def save(self, commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']    

        if commit:
            user.save()

        return user 