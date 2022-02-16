from multiprocessing import get_context
from webbrowser import get
from django.shortcuts import render, HttpResponse
from .models import Producto
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
    model = Producto
    template_name = 'productos_app/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
    