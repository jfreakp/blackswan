from django.contrib import admin
from .models import Categoria, Producto, Carrito
from registration.models import Persona
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Persona)