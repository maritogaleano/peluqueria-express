from django.db import models
from cliente.models import Clientes
from empleado.models import Empleado
from servicios.models import Servicio
from simple_history.models import HistoricalRecords


class Agenda(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, verbose_name='Cliente')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name='Profesional')
    servicio = models.ManyToManyField(Servicio, verbose_name='Servicios')
    fecha_agendada = models.DateTimeField(verbose_name='Fecha programada')
    hora_servicio = models.TimeField(verbose_name="Hora del servicio", null=True)
    observaciones = models.CharField(max_length=250, verbose_name="Observaciones")
    history = HistoricalRecords()


    def __str__(self):
        return self.servicio

    class Meta:
        db_table = 'citas'

