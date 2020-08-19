from .forms import ClienteForm
from .models import Clientes
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from sweetify.views import SweetifySuccessMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import sweetify


class ClienteAdd(SweetifySuccessMixin,CreateView):
    model = Clientes
    form_class = ClienteForm
    template_name = 'clientes/ficha.html'
    success_url = reverse_lazy('clientes:listado_clientes')
    success_message = 'Agregado correctamente'


class ClienteUpdate(SweetifySuccessMixin,UpdateView):
    model = Clientes
    form_class = ClienteForm
    template_name = 'clientes/ficha.html'
    success_url = reverse_lazy('clientes:listado_clientes')
    success_message = 'Actualizado correctamente'

from django.http import HttpResponse, JsonResponse

@csrf_exempt
def eliminar_cliente(request):
    try:
        client = Clientes.objects.get(pk=request.POST['id'])
        client.estado = False
        client.save()
        return JsonResponse({'messaje':'clkient delete without problems'})
    except Exception as e:
         return JsonResponse({'error': str(e)})


class ListadoClientes(ListView):
    model = Clientes
    form_class = ClienteForm
    template_name = 'clientes/listado.html'

    def get_queryset(self):
       return Clientes.objects.order_by('id').filter(estado=True)

  
     

sweetify.DEFAULT_OPTS = {
            'showConfirmButton':False,
            'timer': 3500,
            'allowOutsideClick': True,
            'confirmButtonText': 'OK',
        }