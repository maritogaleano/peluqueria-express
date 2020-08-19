from pel_express.servicios.models import Servicio
from pel_express.trabajos.models import Trabajos

def addWork(request):
    if request.method == 'POST':
        work = Trabajos()
        work.cliente = request.POST['cliente_id']
        work.empleado = request.POST['empleado_id']
        work.cantidad = request.POST['cantidad']
        work.total_servicio = 0;
        for x in range (len(request.POST.getlist('servicio_id'))):
            srvc = Servicio.objects.get(pk=request.POST.getlist('servicio_id')[x])
            work.servicio.add(srvc)
            work.total_servicio = work.total_servicio + srvc.precio 
        work.save()
        sweetify.success(request, 'Trabajo agregado correctamente')
        return redirect('some.url.here')
    else:
        return render('form.html')