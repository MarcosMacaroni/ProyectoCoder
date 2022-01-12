
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields


class FormularioUsuarios(forms.Form):
    nombre= forms.CharField()
    apellido=forms.CharField()
    dni=forms.IntegerField()

class FormularioTurno(forms.Form):
    nombre= forms.CharField()
    actividad=forms.CharField()
    fecha=forms.DateTimeField(help_text='Formato: DD/MM/AA HH:MM:SS')
class RegistroUsuariosForms(UserCreationForm):
    email=forms.EmailField(label='Email', max_length=30, help_text='')
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text='Minimo 8 digitos, utilizar letras y numeros')
    password2=forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput, help_text='')
    class Meta: 
        model= User
        fields= ['username','password1','password2','email',]

class EditarUsuarioForms(UserCreationForm):
    email=forms.EmailField(label='Modificar Email', max_length=30, help_text='')
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text='')
    password2=forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput, help_text='')
    last_name= forms.CharField(label='Apellido', help_text='')
    first_name=forms.CharField(label='Nombre', help_text='')
    class Meta: 
        model= User
        fields= ['email','password1','password2', 'last_name','first_name']

class AvatarCreationForm(forms.Form):
    avatar= forms.ImageField()      
        
