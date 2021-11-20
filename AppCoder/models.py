from django.db import models

# Create your models here.

class Curso (models.Model):
    nombre=models.CharField(max_length=20)
    camada=models.IntegerField()
class Estudiantes(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()
class Profesor (models.Model):
    ...