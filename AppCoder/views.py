from typing import ContextManager
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import password_changed
from django.db.models import fields
from django.db.models.fields import DateTimeField
from django.db.models.lookups import IContains
from django.views.generic.edit import CreateView, UpdateView
from .forms import AvatarCreationForm, FormularioTurno,FormularioUsuarios, RegistroUsuariosForms, EditarUsuarioForms
from .models import Avatar, Usuarios, Turnos
from django.db.models import Q
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate
from django.views.generic import DetailView, DeleteView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.

def inicio(request):

    return render(request,'AppCoder/index.html')

def ver_paginas(request):

    return render(request,'AppCoder/paginas.html')

def about(request):
    
     return render(request,'AppCoder/about.html')

def crear_usuario(request):
    usuario=None
    if request.method == "POST":
        formulario=FormularioUsuarios(request.POST,request.FILES)
        if formulario.is_valid():
            dato_usuario=formulario.cleaned_data
            usuario=Usuarios(nombre=dato_usuario['nombre'],apellido=dato_usuario['apellido'],dni=dato_usuario['dni'])
            usuario.save()
            mensaje='Cliente creado con exito'
            return render(request,'AppCoder/index.html', {'mensaje_usuario':mensaje})
    else:
        formulario=FormularioUsuarios()        
    return render(request,'AppCoder/crear_cliente.html', {'usuario':usuario, 'formulario': formulario})

@login_required
def lista_usuarios(request):
    usuarios=None
    error=None
    if request.method == 'GET':
        dni=request.GET.get('dni', '')
        if dni == '':
            usuarios=Usuarios.objects.all()
        else:
            try:
                dni=int(dni)
                usuarios=Usuarios.objects.filter(dni=dni)
            except:
                error="Ingresar dni sin puntos o letras"
    return render(request,'AppCoder/listar_usuarios.html',{'usuarios': usuarios, 'error':error})

@login_required    
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
    return render(request,'AppCoder/crear_turno.html',{'turno':turno, 'formulario': formulario}) 
 

def login_user(request):  
    if request.method == 'POST':
        
        form=AuthenticationForm(request,request.POST) 
       
        if form.is_valid():
    
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request,'AppCoder/index.html', {'formulario': form, 'mensaje':f'Te logueaste con exito {user}', 'error':True})
            else:
                return render(request,'AppCoder/login.html', {'formulario': form, 'mensaje': "Error, datos incorrectos", 'error':True})
        else:
            return render(request,'AppCoder/login.html', {'formulario': form, 'mensaje':"Formulario erroneo", 'error':True})
        
    form=AuthenticationForm 
    return render(request, 'AppCoder/login.html',{'formulario': form, 'mensaje':'', 'error':False})

def register_user(request):  
    if request.method == 'POST':
        
        form=RegistroUsuariosForms(request.POST) 
       
        if form.is_valid():
    
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, 'AppCoder/index.html',{'formulario': form, 'tiene_mensaje':True, 'mensajeregister':f'Se creo el Usuario: {username}'})
    form=RegistroUsuariosForms()
    return render(request, 'AppCoder/register.html',{'formulario': form, 'mensaje':'', 'error':False})

@login_required
def editar_user(request):  
    
    usuario=request.user
    
    if request.method == 'POST':
        
        form=EditarUsuarioForms(request.POST) 
       
        if form.is_valid():
            
            datos=form.cleaned_data
            
            usuario.email = datos['email']
            usuario.password1 = datos['password1']
            usuario.password2 = datos['password2']
            usuario.first_name= datos['first_name']
            usuario.last_name= datos['last_name']
            usuario.save()
            
            return render(request, 'AppCoder/index.html',{'tiene_mensaje':True, 'mensajeregister':f'Se edito correctamente'})
    else:
        form=EditarUsuarioForms(initial={'email':usuario.email, 'first_name':usuario.first_name,'last_name':usuario.last_name})

    
    return render(request, 'AppCoder/editar_user.html', {'formulario':form,'usuario':usuario})

@login_required
def editar_avatar(request):
    usuario=request.user
    
    if request.method == 'POST':
        
        form=AvatarCreationForm(request.POST,request.FILES) 
       
        if form.is_valid():
            
            avatar = Avatar(user=usuario, avatar=form.cleaned_data['avatar'])
            avatar.save()
            
            return render(request, 'AppCoder/index.html',{'tiene_mensaje':True, 'mensajeregister':f'Se cargo correctamente el avatar', 'url_avatar': avatar.avatar.url})
    else:
        form=AvatarCreationForm()

    
    return render(request, 'AppCoder/editar_avatar.html', {'formulario':form })
class UsuarioDetailView(DetailView):
    model= Usuarios
    template_name= 'AppCoder/detalle_cliente.html'
    
class UsuarioDeleteView(DeleteView):
    model = Usuarios
    success_url= '/'
class TurnoListView(ListView):
    model= Turnos
    template_name= 'AppCoder/listar_turnos.html'

class TurnoDeleteView(DeleteView):
    model=Turnos
    success_url='/lista_turnos/'

class ClienteUpdateView(UpdateView):
    model= Usuarios
    template_name="AppCoder/editar_cliente.html"
    fields= ['nombre', 'apellido', 'dni']
    success_url="/"

class AvatarListView(ListView):
    model=Avatar
    template_name='AppCoder/perfil.html'
    
    

    
    


