from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from ventas_app.views import AgregarCarrito, CarritoListView, EliminarCarrito,CorreoEnvListView, CorreoListView
from . import views


urlpatterns = [
    path('ventas/agregar/<int:producto_id>',views.AgregarCarrito,name='agregar_carrito'),
    path('ventas/eliminar/<int:carrito_id>',views.EliminarCarrito,name='eliminar_carrito'),
    path('ventas/correoenviado/',CorreoEnvListView.as_view(),name='correo_enviado'),
    path('correo/',CorreoListView.as_view(),name='correo'),
    path('carrito/',CarritoListView.as_view(),name='carrito'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)