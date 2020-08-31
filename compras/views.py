from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, FormView
from django.http import JsonResponse
from django.shortcuts import render
from .forms import BoletaForm
from .models import Almacen
# Create your views here.

class NuevaBoleta(CreateView):
    template_name="compras/nueva-boleta.html"
    form_class = BoletaForm

    def post(self,request,*args,**kwargs):
        message = "xD"
        try:
            form = BoletaForm(request.POST)
            form.is_valid()
            form.save()
        except Exception as e:
            message=str(e)
            for field, errors in form.errors.items():
                message += ";"+str(field)+"<>"+str(errors)
        return JsonResponse({"message":message,"data":request.POST},safe=False)

def BuscarAlmacen(request):
    productos = list(Almacen.objects.filter(nombre__istartswith=request.GET.get("q")).values()[:10])
    return JsonResponse(productos,safe=False)







    # def post(self, request, *args, **kwargs):
    # try:
    #     super().post(request, *args, **kwargs)
    # except IntegrityError:
    #     messages.add_message(request, messages.ERROR,
    #                          'You already have registered a Client with this name. ' + \
    #                          'All of your Client names must be unique.')
    #     return render(request, template_name=self.template_name, context=self.get_context_data())