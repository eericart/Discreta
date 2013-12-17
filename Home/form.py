from django import forms
from django.contrib.auth.models import User


class Contact(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput,label='Full Name')
    email = forms.EmailField(widget=forms.EmailInput(),label='Email')
    asunto = forms.CharField(widget=forms.TextInput(),label='Asunto')
    Texto = forms.CharField(widget=forms.Textarea(), min_length=5, max_length=500)
    cc_myself = forms.BooleanField(required=False,label='CC My Selft')

