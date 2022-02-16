from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    precio_normal = models.IntegerField(blank=False)
    precio_oferta = models.IntegerField(blank=False)
    imagen = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.nombre