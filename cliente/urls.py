from django.urls import path
from .views import *


app_name = 'clientes'


urlpatterns = [

    path('listado/', ListadoClientes.as_view(), name='listado_clientes'),
    path('nuevo/', ClienteAdd.as_view(), name='nuevo_cliente'),
    path('edit/<int:pk>/', ClienteUpdate.as_view(), name='cliente_update'),
    path('delete/', eliminar_cliente, name='cliente_delete'),
]