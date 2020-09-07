from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, FormView
from .business_logic.boleta import saveBoletaFromRequest
from django.shortcuts import render, redirect
from .models import Almacen, Proveedor
from django.http import JsonResponse
from django.urls import reverse_lazy
from .forms import *
import sweetify

# Create your views here.


class NuevaBoleta(CreateView):
    template_name = "compras/nueva-boleta.html"
    form_class = BoletaForm

    def post(self, request, *args, **kwargs):
        response = {"status": "success", "details": ""}
        try:
            form = BoletaForm(request.POST)
            if form.is_valid():
                boleta = form.save(commit=False)
                saveBoletaFromRequest(boleta, request.POST)
            else:
                for field, errors in form.errors.items():
                    response["details"] += ";"+str(field)+"<>"+str(errors)
        except Exception as e:
            response["status"] = "error"
            response["details"] = str(e)
        return JsonResponse(response, safe=False)


def BuscarAlmacen(request):
    productos = list(Almacen.objects.filter(
        nombre__istartswith=request.GET.get("q")).values()[:20])
    return JsonResponse(productos, safe=False)


# Proveedores

def proveedores(request):
    return render(request, 'compras/proveedores.html')

def new_provider(request):
    try:
        pro = Proveedor()
        pro.nombre = request.POST["name"]
        pro.save()
        sweetify.success(request, 'Proovedor Guardado Correctamente')
    except Exception as e:
        sweetify.error(request, str(e))
    
    return redirect('compras:proveedores')

class ProveedorUpdate(sweetify.views.SweetifySuccessMixin,UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'compras/edit-provider.html'
    success_url = reverse_lazy('compras:proveedores')
    success_message = 'Actualizado correctamente'

def delete_provider(request):
    try:
        pro = Proveedor.objects.get(pk=request.POST['id'])
        pro.delete()
        return JsonResponse({'messaje': 'Proveedor eliminado sin problemas'})
    except Exception as e:
        return JsonResponse({'error': str(e)})


def BuscarProveedor(request):
    query = Proveedor.objects.values()
    if request.GET.get("origin") != "dataTable":
        proveedores = list(query.filter(
            nombre__istartswith=request.GET.get("q")).values()[:20])
    proveedores = list(query)
    return JsonResponse(proveedores, safe=False)
