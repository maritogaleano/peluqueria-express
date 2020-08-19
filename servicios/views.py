from .models import Servicio
from .forms import ServicioForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from sweetify.views import SweetifySuccessMixin
import sweetify


class ListadoServicios(ListView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicios/listado.html'


class ServicioAdd(SweetifySuccessMixin,CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicios/nuevo.html'
    success_url = reverse_lazy('servicios:listado_servicios')
    success_message = 'Agregado correctamente'