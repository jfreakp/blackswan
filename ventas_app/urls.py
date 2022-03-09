from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from ventas_app.views import AgregarCarrito, CarritoListView, EliminarCarrito
from . import views


urlpatterns = [
    path('ventas/agregar/<int:producto_id>',views.AgregarCarrito,name='agregar_carrito'),
    path('ventas/eliminar/<int:carrito_id>',views.EliminarCarrito,name='eliminar_carrito'),
    path('carrito',CarritoListView.as_view(),name='carrito'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)