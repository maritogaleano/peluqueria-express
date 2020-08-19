from django.db import models
from simple_history.models import HistoricalRecords

class Servicio (models.Model):
    nombre = models.CharField(max_length=200, unique=True, verbose_name="Servicio")
    precio = models.FloatField(default=0)
 

    def __str__(self):
         return self.nombre
    
    class Meta:
        db_table = 'servicios'
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
