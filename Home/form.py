from django import forms
from django.contrib.auth.models import User
from account.models import Materia

CHOICE= (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))

class Contact(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput,label='Full Name')
    email = forms.EmailField(widget=forms.EmailInput(),label='Email')
    asunto = forms.CharField(widget=forms.TextInput(),label='Asunto')
    Texto = forms.CharField(widget=forms.Textarea(), min_length=5, max_length=500)
    cc_myself = forms.BooleanField(required=False,label='CC My Selft')

class RateForm (forms.Form):
    subject= forms.ModelChoiceField(queryset=Materia.objects.all(), required=False,widget=forms.Select())
    vote = forms.ChoiceField(widget=forms.RadioSelect,label='Vote',choices=CHOICE)