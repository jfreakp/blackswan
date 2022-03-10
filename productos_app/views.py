from contextvars import Context
from multiprocessing import get_context
from webbrowser import get
from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.views.generic import ListView
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
        productos = Producto.objects.all()
        categorias = Categoria.objects.all()
        context = {"productos":productos, "categorias":categorias}
        return context
    
def ListarGenero(request, genero):
    template_name = 'productos_app/tienda.html'
    def get_queryset(self):
        productos = Producto.objects.filter(genero=genero).all()
        categorias = Categoria.objects.all()
        context = {"productos":productos, "categorias":categorias}
        return redirect('shop', context)
    
def About(request):    
    return render(request, 'productos_app/about.html')

def Contacto(request):    
    return render(request, 'productos_app/contacto.html')