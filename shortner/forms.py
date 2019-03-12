from django import forms
from django.core.validators import URLValidator, EmailValidator
from django.forms import CharField


class URLField(CharField):
    default_validators = [URLValidator]


class EmailField(CharField):
    default_validators = [EmailValidator]


class SubmitURLForm(forms.Form):
    URL_Field = forms.URLField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Ex: https://facebook.com'}))

class SignupForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':'Enter your username'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder':'Ex: you@example.com'}))
    password = forms.CharField(label ='Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter a Password'}))
    confirmPassword = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter your password again'}))
