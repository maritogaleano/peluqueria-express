from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, FormView
from .business_logic.boleta import saveBoletaFromRequest
from .models import Almacen, Proveedor
from django.http import JsonResponse
from django.shortcuts import render
from .forms import BoletaForm
# Create your views here.


class NuevaBoleta(CreateView):
    template_name = "compras/nueva-boleta.html"
    form_class = BoletaForm

    def post(self, request, *args, **kwargs):
        response = {"status":"success","details":""}
        try:
            form = BoletaForm(request.POST)
            print("here")
            if form.is_valid():
                print("enter here")
                boleta = form.save(commit=False)
                saveBoletaFromRequest(boleta, request.POST)
            else:
                for field, errors in form.errors.items():
                    response["details"] += ";"+str(field)+"<>"+str(errors)
        except Exception as e:
            response["status"]="error"
            response["details"] = str(e)
        return JsonResponse(response, safe=False)

def BuscarAlmacen(request):
    productos = list(Almacen.objects.filter(
        nombre__istartswith=request.GET.get("q")).values()[:20])
    return JsonResponse(productos, safe=False)


def BuscarProveedor(request):
    proveedores = list(Proveedor.objects.filter(
        nombre__istartswith=request.GET.get("q")).values()[:10])
    return JsonResponse(proveedores, safe=False)

    # def post(self, request, *args, **kwargs):
    # try:
    #     super().post(request, *args, **kwargs)
    # except IntegrityError:
    #     messages.add_message(request, messages.ERROR,
    #                          'You already have registered a Client with this name. ' + \
    #                          'All of your Client names must be unique.')
    #     return render(request, template_name=self.template_name, context=self.get_context_data())
