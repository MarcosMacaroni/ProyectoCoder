from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    dni=models.IntegerField()
    
    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido} DNI: {self.dni}'
    
class Turnos(models.Model):
    nombre = models.CharField(max_length=20)
    actividad= models.CharField(max_length=20)
    fecha=models.DateTimeField('%d/%m/$y')
    
    def __str__(self):
        return f'Nombre: {self.nombre} Actividad: {self.actividad} Fecha: {self.fecha}'
    
class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='avatares',null=False, blank=True)

