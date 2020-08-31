from django.urls import path
from .views import *


app_name = 'compras'


urlpatterns = [
    path('boleta-nueva/', NuevaBoleta.as_view(), name='boleta_nueva'),
    path('producto/busqueda/', BuscarAlmacen, name='producto_busqueda'),
]