from django import forms
from account.models import UserProfile,Carrera,Materia


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))


class RegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    lastname = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), min_length=8)
    carrera = forms.ModelChoiceField(queryset=Carrera.objects.all(),required=True,empty_label=None)




class RegistrationFormC(forms.Form):

    materias = forms.ModelMultipleChoiceField(queryset=Materia.objects.all(), required=False,widget=forms.CheckboxSelectMultiple())