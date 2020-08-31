from django.db import models
from compras.models import Almacen
# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=25, default=None, null=False)
    detalle = models.TextField(default="")
    consumo_insumo = models.ManyToManyField(
        Almacen, through="Consumo", related_name="insumo_en_servicio")
    precio = models.FloatField(default=0)

    def __str__(self):
        return str(self.pk)+":"+self.nombre

    class Meta:
        db_table = 'servicio'
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'


class Consumo(models.Model):
    insumo = models.ForeignKey(
        Almacen, related_name="insumo_consumido", on_delete=models.CASCADE)
    servicio = models.ForeignKey(
        Servicio, related_name="servicio_consumidor", on_delete=models.CASCADE)
    cantidad = models.IntegerField(
        default=0, help_text="cantidad de insumo que se utiliza en el servicio")

    def __str__(self):
        return self.insumo + "<>"+self.servicio

    class Meta:
        db_table = 'consumo'
        verbose_name = 'Consumo'
        verbose_name_plural = 'consumos'

class Venta(models.Model):
    fecha_compra = models.DateField(default=None, null=False)
    # productos = models.ManyToManyField()
    sub_total = models.FloatField(default=0)
    impuesto = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return str(self.pk)+str(self.fecha_compra)