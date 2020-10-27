from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, FormView,DetailView
from .business_logic.boleta import saveBoletaFromRequest
from .models import Almacen, Proveedor, BoletaCompra
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from .forms import *
import sweetify

# Create your views here.

# boletas


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
                response["status"] = "error"
                for field, errors in form.errors.items():
                    response["details"] += str(field)+" : "+str(errors.as_text()+"    ")
        except Exception as e:
            if hasattr(boleta, 'pk'):
                boleta.delete()
            response["status"] = "error"
            response["details"] = str(e)
        return JsonResponse(response, safe=False)


def boletas(request):
    return render(request, 'compras/boletas.html')

class BoletaDetail(DetailView):
    model = BoletaCompra
    template_name = 'compras/detail-boleta.html'
    context_object_name = 'boleta'

def boletas_json(request):
    boletas = list(BoletaCompra.objects.values(
        'id','fecha_compra', 'facturado', 'sub_total', 'impuesto_total', 'comentarios', 'total', 'proveedor__nombre'))
    return JsonResponse(boletas, safe=False)

# Proveedores


def proveedores(request):
    return render(request, 'compras/proveedores.html')


def new_provider(request):
    print(request.POST)
    try:
        pro = ProveedorForm(request.POST)
        pro = pro.save()
        sweetify.success(request, 'Proovedor Guardado Correctamente')
    except Exception as e:
        sweetify.error(request, str(e))
    if 'origin' in request.POST:
        return JsonResponse({'id':pro.pk},safe=False)
    return redirect('compras:proveedores')


class ProveedorUpdate(sweetify.views.SweetifySuccessMixin, UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'compras/edit-provider.html'
    success_url = reverse_lazy('compras:proveedores')
    success_message = 'Actualizado correctamente'

    def post(self,*args,**kwargs):
        super().post(*args, **kwargs)


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
        query = query.filter(
            nombre__istartswith=request.GET.get("q")).values()[:20]
    proveedores = list(query)
    return JsonResponse(proveedores, safe=False)

# Products


def almacenes(request):
    return render(request, 'compras/almacenes.html')


def BuscarAlmacen(request):
    query = Almacen.objects.values()
    if request.GET.get("origin") != "dataTable":
        query = query.filter(
            nombre__istartswith=request.GET.get("q")).values()[:20]
    productos = list(query)
    return JsonResponse(productos, safe=False)


def new_product(request):
    try:
        form = ProductForm(request.POST)
        product = form.save()
        sweetify.success(request, 'Almacen Guardado Correctamente')
    except Exception as e:
        sweetify.error(request, str(e))
    if 'origin' in request.POST:
        return JsonResponse({'id':product.pk},safe=False)
    return redirect('compras:almacenes')


class ProductUpdate(sweetify.views.SweetifySuccessMixin, UpdateView):
    model = Almacen
    form_class = ProductForm
    template_name = 'compras/edit-product.html'
    success_url = reverse_lazy('compras:almacenes')
    success_message = 'Actualizado correctamente'


def delete_products(request):
    try:
        alm = Almacen.objects.get(pk=request.POST['id'])
        alm.delete()
        return JsonResponse({'messaje': 'Almacen eliminado sin problemas'})
    except Exception as e:
        return JsonResponse({'error': str(e)})
