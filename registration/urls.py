from django.urls import path
from .views import RegistroView, Persona_nueva
from . import views

urlpatterns = [
    path('signup/', RegistroView.as_view(), name="registro"),
    #path('profile/', ProfileUpdate.as_view(), name="profile"),
    #path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    #persona urls
    path('persona/nueva', views.Persona_nueva, name='persona_nueva'),
    path('persona/detalle/', views.Persona_detalle, name='persona_detalle'),
]