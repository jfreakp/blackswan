from django.urls import path
from productos_app.views import HomeListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',HomeListView.as_view(),name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)