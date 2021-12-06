from django.urls import path
from AppCoder import views

urlpatterns = [
      path('', views.inicio, name='Inicio'),
      path('crear_usuario/', views.crear_usuario, name='link1'),
      path('lista_usuarios/', views.lista_usuarios, name='listausuarios'),
      path('turnos/', views.turnos, name='turnos'),
      path('link4/', views.link4, name='link4'),
]