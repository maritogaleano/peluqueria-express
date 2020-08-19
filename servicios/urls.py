from django.urls import path
from .views import *


app_name = 'servicios'


urlpatterns = [

    path('listado/', ListadoServicios.as_view(), name='listado_servicios'),
    path('nuevo/', ServicioAdd.as_view(), name='nuevo_servicio'),
] 