from django.db import models
from simple_history.models import HistoricalRecords
from cliente.models import Clientes
from servicios.models import Servicio
from empleado.models import Empleado


class Trabajos (models.Model):
    fecha_servicio = models.DateField(auto_now_add=True, null=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    servicio = models.ManyToManyField(Servicio)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0, verbose_name="Cantidad")
    total_servicio = models.FloatField(default=0, verbose_name="Total Servicio")
    history = HistoricalRecords()

    def __str__(self):
         return self.nombre
    
    class Meta:
        db_table = 'trabajos'
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'

