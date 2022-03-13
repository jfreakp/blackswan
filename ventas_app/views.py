from pickle import NONE
from django.shortcuts import redirect
from django.contrib import messages
from productos_app.models import Carrito, Producto
from django.views.generic import ListView
from django.core import serializers
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User


# Create your views here.

def email(usuario):
    carritos = Carrito.objects.filter(activo=False)
    precio_subtotal = 0
    precio_total = 0
    for i in carritos:
        precio_subtotal = 0
        precio_subtotal = i.precio*i.cantidad
        precio_total += precio_subtotal
        print('Pedido para enviar:')
        print(precio_total)
    print('--------------------')
    context = {'carritos': carritos, 'precio_total': precio_total}
    html_template = 'ventas_app/correo.html'
    html_message = render_to_string(html_template, {'context': context, })
    subject = 'Blackswuan te saluda.'
    #message = 'Hola Juan Pablo buenas noches.'

    email_from = usuario.email
    recipient_list = [settings.EMAIL_HOST_USER, ]
    message = EmailMessage(subject, html_message, email_from, recipient_list)
    # this is required because there is no plain text email message
    message.content_subtype = 'html'
    message.send()
    return redirect('shop')


def AgregarCarrito(request, producto_id):
    producto = Producto.objects.filter(id=producto_id)
    carrito = Carrito.objects.filter(
        producto=producto_id).filter(usuario=request.user).first()
    # email()
    precio_producto = 0
    if producto[0].precio_oferta == 0:
        precio_producto = producto[0].precio_normal
    else:
        precio_producto = producto[0].precio_oferta
    if(carrito is None):
        carrito = Carrito(nombre=producto[0].nombre, producto=producto_id,
                          imagen=producto[0].imagen, usuario=request.user, cantidad=1,  precio=precio_producto)
        carrito.save()
        print('Save')
    else:
        carrito.cantidad += 1
        carrito.save()
        print('update')
    messages.success(request, 'Se agrego el producto ')
    return redirect('shop')


def EliminarCarrito(request, carrito_id):
    print('Carrito: '+str(carrito_id))
    try:
        record = Carrito.objects.get(id=carrito_id)
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
            precio_subtotal = i.precio*i.cantidad
            precio_total += precio_subtotal
        context = {'carritos': carritos, 'precio_total': precio_total}
        print(context)
        return context


class CorreoEnvListView(ListView):
    template_name = 'ventas_app/correo_enviado.html'

    def get_queryset(self):
        usuario = User.objects.get(username=self.request.user)
        carritos = Carrito.objects.filter(activo=False)
        precio_subtotal = 0
        precio_total = 0
        for i in carritos:
            precio_subtotal = 0
            precio_subtotal = i.precio*i.cantidad
            precio_total += precio_subtotal
        context = {'carritos': carritos,
                   'precio_total': precio_total, 'usuario':usuario}
        email(usuario)
        return context


class CorreoListView(ListView):
    template_name = 'ventas_app/correo.html'

    def get_queryset(self):
        usuario = User.objects.get(username=self.request.user)
        carritos = Carrito.objects.filter(activo=False)
        precio_subtotal = 0
        precio_total = 0
        for i in carritos:
            precio_subtotal = 0
            precio_subtotal = i.precio*i.cantidad
            precio_total += precio_subtotal
        context = {'carritos': carritos,
                   'precio_total': precio_total, 'email': usuario.email,
                   'nombre': usuario.first_name + ' ' + usuario.last_name, 'usuario':usuario.username}
        print(usuario.email)
        return context
