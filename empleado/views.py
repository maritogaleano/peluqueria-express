from .models import Empleado
from .forms import EmpleadoForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from sweetify.views import SweetifySuccessMixin
import sweetify


class ListaEmpleados(ListView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/listado_empleados.html'


class EmpleadoAdd(SweetifySuccessMixin,CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/ficha.html'
    success_url = reverse_lazy('profesionales:listado_empleados')
    success_message = 'Agregado correctamente'