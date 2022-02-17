from django.urls import path
from productos_app.views import HomeListView, ShopListView
from django.conf import settings
from django.conf.urls.static import static
from productos_app.views import *
from . import views


urlpatterns = [
    path('',HomeListView.as_view(),name='home'),
    path('about/',views.About,name='about'),
    path('contact/',views.Contacto,name='contact'),
    path('shop/',ShopListView.as_view(),name='shop'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)