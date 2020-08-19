from django.urls import path
from .views import *


app_name = 'profesionales'


urlpatterns = [

    path('listado/', ListaEmpleados.as_view(), name='listado_empleados'),
    path('nuevo/', EmpleadoAdd.as_view(), name='nuevo_empleado'),

]