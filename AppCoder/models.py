from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    dni=models.IntegerField()
    imagen=models.ImageField(upload_to='usuarios', null=True, blank=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido}'
    
class Turnos(models.Model):
    nombre = models.CharField(max_length=20)
    actividad= models.CharField(max_length=20)
    fecha=models.DateTimeField('%d/%m/$y')
    
    def __str__(self):
        return f'Nombre: {self.nombre} Actividad: {self.actividad} Fecha: {self.fecha}'
    
class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='avatares',null=False, blank=True)

class AvatarUsuario(models.Model):
    usuario= models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='usuario',null=False, blank=True)

