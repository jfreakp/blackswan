from tkinter import TRUE
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.nombre

class Genero(models.TextChoices):
        MASCULINO = 'M', ('Masculino')
        FEMENINO = 'F', ('Femenino')
        

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,blank = False, on_delete=models.CASCADE,default=1)
    nombre = models.CharField(max_length=100, blank=False)
    genero = models.CharField(max_length=1,blank=False, choices=Genero.choices, default=Genero.MASCULINO)
    talla = models.CharField(max_length=20, blank=False)
    precio_normal = models.PositiveIntegerField(blank=False)
    precio_oferta = models.PositiveIntegerField(blank=False)
    stock = models.PositiveIntegerField(blank=False,default=1)    
    imagen = models.ImageField(upload_to='images/p/',blank=False)
    vigente = models.BooleanField(default=True, blank=False)
    
    def __str__(self):
        return self.nombre
    

    
#class ImagenProducto(models.Model):
#    producto = models.ForeignKey(Producto, blank=False, on_delete=models.CASCADE)
#    nombre = models.CharField(max_length=100,blank=False)    
#    imagen = models.ImageField(upload_to='images'+producto.nombre+'/s/')
#    
#    def __str__(self):
#        return self.nombre
#    