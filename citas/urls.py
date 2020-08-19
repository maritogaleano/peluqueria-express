from django.urls import path
from .views import *


app_name = 'agendamientos'


urlpatterns = [

   path('nuevo/', NuevaAgenda.as_view(), name='nueva_agenda'),
   path('calendario/', Calendar, name='calendario'),

]