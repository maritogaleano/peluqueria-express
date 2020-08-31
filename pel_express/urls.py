from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView
from login.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('login/', Login.as_view()),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('clientes/', include('cliente.urls')),
    path('profesionales/', include('empleado.urls')),
    path('servicios/', include('servicios.urls')),
    path('agendamientos/', include('citas.urls')),
    path('compras/', include('compras.urls')),
    #path('', TemplateView.as_view(template_name='base.html'),name="index"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
