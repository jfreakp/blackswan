from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):
    usuario = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=False, default=' ')
    apellido = models.CharField(max_length=100, blank=False, default=' ')
    celular = models.CharField(max_length=20, blank=False, default=' ')
    telefono = models.CharField(max_length=20, blank=False, default=' ')
    foto = models.ImageField(upload_to='fotos/', blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
