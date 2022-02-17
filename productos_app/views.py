from contextvars import Context
from multiprocessing import get_context
from webbrowser import get
from django.shortcuts import render
from .models import Producto, Categoria
from django.views.generic import ListView
from itertools import chain
from operator import attrgetter

# Create your views here.
#def home(request):
#    catagorias = Categoria.objects.all()
#    data = {
#        'titulo':'Catagorias',
#        'cursos':catagorias
#    }
#    return render(request, 'productos_app/home.html',data)

class HomeListView(ListView):
#   model = Model
#   template_name = 'productos_app/home.html'
#   
#   def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       context['images'] = models.ImagenProducto.objects.all()
#       print(context)
#       return context
    template_name = 'productos_app/home.html'
    def get_queryset(self):
        context = Producto.objects.all() 
        return context
    
class ShopListView(ListView):
    template_name = 'productos_app/tienda.html'
    def get_queryset(self):
        data = {
            'productos':Producto.objects.all,
            'categorias':Categoria.objects.all
        }
        return data
    
def About(request):    
    return render(request, 'productos_app/about.html')

def Contacto(request):    
    return render(request, 'productos_app/contacto.html')