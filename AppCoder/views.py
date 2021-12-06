from typing import ContextManager
from django.db.models.fields import DateTimeField
from django.db.models.lookups import IContains
from AppCoder.forms import FormularioUsuarios,FormularioTurno
from AppCoder.models import Usuarios, Turnos
from django.db.models import Q
from django.shortcuts import render
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
            usuario=Usuarios(nombre=dato_usuario['nombre'],apellido=dato_usuario['apellido'],dni=dato_usuario['dni'])
            usuario.save()
            mensaje='Cliente creado con exito'
            return render(request,'AppCoder/index.html', {'mensaje':mensaje})
    else:
        formulario=FormularioUsuarios()        
    return render(request,'AppCoder/link1.html', {'usuario':usuario, 'formulario': formulario})

def lista_usuarios(request):
    usuarios=Usuarios.objects.all()
    return render(request,'AppCoder/listar_usuarios.html',{'usuarios': usuarios})
    
def turnos(request):
    turno=None
    if request.method == "POST":
        formulario=FormularioTurno(request.POST)
        if formulario.is_valid():
            dato_turno=formulario.cleaned_data
            turno=Turnos(nombre=dato_turno['nombre'],actividad=dato_turno['actividad'],fecha=dato_turno['fecha'])
            turno.save()
            mensaje2='Turno guardado para el dia '
            return render(request,'AppCoder/index.html', {"turno": turno,"mensaje2":mensaje2})
    else:
        formulario=FormularioTurno()        
    return render(request,'AppCoder/link3.html',{'turno':turno, 'formulario': formulario}) 

def link4(request):
    return render(request,'AppCoder/link4.html',{})    
    
    





