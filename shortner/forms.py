from django import forms
from django.core.validators import URLValidator
from django.forms import CharField

class URLField(CharField):
    default_validators = [URLValidator]

class SubmitURLForm(forms.Form):
    URL_Field = forms.URLField(label='')
    
        