from django.urls import path
from .views import *

app_name = 'compras'

urlpatterns = [
    path('boleta-nueva/', NuevaBoleta.as_view(), name='boleta_nueva'),
    path('producto/busqueda/', BuscarAlmacen, name='producto_busqueda'),
    path('producto/almacenes/', almacenes, name='almacenes'),
    path('producto/nuevo', new_product, name='new_product'),
    path('producto/<int:pk>/', ProductUpdate.as_view(), name='edit_products'),
    path('producto/eliminar/', delete_products, name='delete_products'),
    path('proveedores/', proveedores, name='proveedores'),
    path('proveedor/busqueda/', BuscarProveedor, name='proveedor_busqueda'),
    path('proveedores/nuevo', new_provider, name='new_provider'),
    path('proveedores/<int:pk>/', ProveedorUpdate.as_view(), name='edit_provider'),
    path('proveedores/eliminar', delete_provider, name='delete_provider'),
]