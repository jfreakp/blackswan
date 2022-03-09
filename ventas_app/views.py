from django.shortcuts import redirect
from django.contrib import messages
from productos_app.models import Carrito, Producto
from django.views.generic import ListView

# Create your views here.

def AgregarCarrito(request, producto_id):    
    producto = Producto.objects.filter(id=producto_id)    
    carrito = Carrito.objects.filter(id=producto_id).filter(usuario=request.user).first()
    print(carrito)
    if(carrito == 'None'):
        print('Ingreso-----------------------------------------')
        carrito = Carrito(nombre=producto[0].nombre,imagen=producto[0].imagen, usuario=request.user,cantidad=carrito.cantidad+1,  precio=20)
        carrito.save()
        print('inserto')
    else:
        print('Ingreso2-----------------------------------------')
        carrito = Carrito(nombre=producto[0].nombre,imagen=producto[0].imagen, usuario=request.user,cantidad=1,  precio=20)
        carrito.save()
        print('udate')
        print('Si existe el producto.')
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
        precio_total = 0
        for i in carritos:
            precio_total+=i.precio
        context = {'carritos': carritos, 'precio_total': precio_total}
        print(context)
        return context