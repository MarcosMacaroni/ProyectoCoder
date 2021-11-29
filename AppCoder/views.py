from typing import ContextManager
from AppCoder.forms import FormularioUsuarios
from AppCoder.models import Usuarios
from django.db.models.query_utils import Q
from django.shortcuts import render
from AppCoder import models
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,'AppCoder/index.html',{})

def crear_usuario(request):
    usuario=None
    if request.method == "POST":
        formulario=FormularioUsuarios(request.POST)
        if formulario.is_valid():
            dato_usuario=formulario.cleaned_data
            usuario=Usuarios(usuario=dato_usuario['usuario'],email=dato_usuario['email'],contraseña=dato_usuario['contraseña'])
            usuario.save()
            formulario=FormularioUsuarios() 
    else:
        formulario=FormularioUsuarios()        
    return render(request,'AppCoder/link1.html', {'usuario':usuario, 'formulario': formulario})

def link2(request):
    return render(request,'AppCoder/link2.html',{})

def link3(request):
    return render(request,'AppCoder/link3.html',{})

def link4(request):
    return render(request,'AppCoder/link4.html',{})    
    
    





