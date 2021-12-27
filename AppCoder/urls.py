from django.urls import path
from .views import UsuarioDetailView, UsuarioDeleteView
from django.contrib.auth.views import LogoutView
from AppCoder import views

urlpatterns = [
      path('', views.inicio, name='inicio'),
      path('paginas/', views.ver_paginas, name='paginas'),
      path('crear_cliente/', views.crear_usuario, name='crear_cliente'),
      path('editar_cliente/', views.crear_usuario, name='editar_cliente'),
      path('lista_usuarios/', views.lista_usuarios, name='listausuarios'),
      path('turnos/', views.turnos, name='turnos'),
      path('accounts/login/',views.login_user, name='login'),
      path('logout/',LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),
      path('eliminar/<int:pk>/', UsuarioDeleteView.as_view(template_name='AppCoder/eliminar_cliente.html'), name='eliminar_cliente'),
      path('register/',views.register_user, name='register'),
      path('editar/',views.editar_user, name='editar'),
      path('editar_avatar/',views.editar_avatar, name='editar_avatar'),
      path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='detalle_cliente'),
      path('about/', views.about, name='about'),
      ]