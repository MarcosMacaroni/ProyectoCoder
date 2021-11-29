from django import forms

class FormularioUsuarios(forms.Form):
    usuario = forms.CharField()
    email=forms.EmailField()
    contraseña=forms.CharField()