from django.db import models
from simple_history.models import HistoricalRecords

class Empleado(models.Model):
    nombre = models.CharField(max_length=150, unique=True, verbose_name="Nombre y Apellido")
    documento = models.CharField(max_length=100, verbose_name="CI / RUC ")
    fecha_nac = models.DateField(verbose_name="Fecha de Nacimiento")
    telefono = models.CharField(max_length=100, verbose_name="Teléfono - Celular")
    email = models.EmailField(max_length=70, verbose_name="Email")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    ciudad = models.CharField(max_length=150, verbose_name="Ciudad")
    history = HistoricalRecords()



    def __str__(self):
         return self.nombre
    
    class Meta:
        db_table = 'empleados'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

