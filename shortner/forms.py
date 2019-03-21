from django import forms
from django.core.validators import URLValidator, EmailValidator
from django.forms import CharField




class SubmitURLForm(forms.Form):
    URL_Field = forms.URLField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Ex: https://facebook.com'}))

class SignupForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':'Enter your username'}))
    email = forms.EmailField()
    password = forms.CharField(label ='Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter a Password'}))
    confirmPassword = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter your password again'}))
