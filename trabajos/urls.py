from django.urls import path
from .views import *


app_name = 'trabajos'


urlpatterns = [

    path('nuevo/', addWork, name='nuevo_trabajo',
    #path('nuevo/', EmpleadoAdd.as_view(), name='nuevo_empleado'),

]