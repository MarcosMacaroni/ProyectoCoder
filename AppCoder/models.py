from django.db import models

# Create your models here.

class Usuarios(models.Model):
    usuario=models.CharField(max_length=20)
    email=models.EmailField()
    contraseña=models.CharField(max_length=20)
    