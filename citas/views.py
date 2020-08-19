from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, ListView
from .models import Agenda
from .forms import AgendaForm
from django.urls import reverse_lazy
from sweetify.views import SweetifySuccessMixin

class NuevaAgenda(SweetifySuccessMixin, CreateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'citas/nuevo_servicio.html'
    success_url = reverse_lazy('clientes:listado_clientes')
    success_message = 'Cita creada correctamente'


def Calendar(request):
    agenda = Agenda.objects.all()
    context = {
        "events": agenda,
    }

    return render(request,'citas/calendario.html', context)
