from pickle import NONE
from django.shortcuts import redirect
from django.contrib import messages
from productos_app.models import Carrito, Producto
from django.views.generic import ListView
from django.core import serializers

# Create your views here.

def AgregarCarrito(request, producto_id):    
    producto = Producto.objects.filter(id=producto_id) 
    carrito = Carrito.objects.filter(producto=producto_id).filter(usuario=request.user).first()
    
    print('----------------')
    print('precio_normal')
    print(producto[0].precio_normal)
    print('precio_oferta')
    print(producto[0].precio_oferta)
    print('----------------')
    precio_producto = 0
    if producto[0].precio_oferta == 0:
        precio_producto= producto[0].precio_normal
    else:
        precio_producto= producto[0].precio_oferta
    if(carrito is None):        
        carrito = Carrito(nombre=producto[0].nombre,producto=producto_id, imagen=producto[0].imagen, usuario=request.user,cantidad=1,  precio=precio_producto)
        carrito.save()
        print('Save')
    else:
        carrito.cantidad +=1 
        carrito.save()
        print('update')
    messages.success(request,'Se agrego el producto ')
    return redirect('shop')

def EliminarCarrito(request, carrito_id):    
    print('Carrito: '+str(carrito_id))
    try:
        record = Carrito.objects.get(id = carrito_id)
        record.delete()
        print("Carrito Eliminado!")
    except:
        print("El carrito no existe.")
    return redirect('carrito')
    
class CarritoListView(ListView):
    template_name = 'ventas_app/carrito.html'
    def get_queryset(self):
        carritos = Carrito.objects.filter(activo=False)
        precio_subtotal = 0        
        precio_total = 0
        for i in carritos:
            precio_subtotal = 0
            precio_subtotal=i.precio*i.cantidad
            precio_total+=precio_subtotal
        context = {'carritos': carritos, 'precio_total': precio_total}
        print(context)
        return context