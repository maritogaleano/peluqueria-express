from django.db import transaction
from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.
# made with love by c4-technologies


class Almacen(models.Model):
    nombre = models.CharField(max_length=25, default=None, null=False)
    detalle = models.TextField(default="")
    precio = models.FloatField(default=0)
    cantidad = models.IntegerField(default=1)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.pk)+":"+self.nombre

    class Meta:
        db_table = 'almacen'
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'
    
    def __alterar_cantidad(self,movimiento,cantidad):
        cantidad = int(cantidad)
        with transaction.atomic():
            if movimiento == "sumar":
                self.cantidad += cantidad
            else:
                self.cantidad -= cantidad     
            self.save()    

    def sumar_almacen(self,cantidad):
        self.__alterar_cantidad("sumar",cantidad)

    def restar_almacen(self,cantidad):
        self.__alterar_cantidad("restar",cantidad)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, default=None, null=False)
    ruc = models.CharField(max_length=20, default=None, null=True, verbose_name="Registro Único Contribuyente")
    direccion = models.CharField(max_length=200, default=None, null=True, verbose_name="Dirección")
    telefono = models.CharField(max_length=25, default=None, null=True, verbose_name="Teléfono - Celular")
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class BoletaCompra(models.Model):
    fecha_compra = models.DateField(default=None, null=False)
    numero_factura = models.CharField(default="0", null=True, max_length=25)
    fecha_facturado = models.DateField(default=None, null=True)
    facturado = models.BooleanField(default=False)
    proveedor = models.ForeignKey(
        Proveedor, related_name="compra_a_proveedor", on_delete=models.CASCADE)
    sub_total = models.FloatField(default=0)
    # impuesto en 10%
    impuesto_total = models.FloatField(default=0)
    comentarios = models.TextField(default="")
    # detalle
    detalles = models.ManyToManyField(
        Almacen, through="DetalleCompra", related_name="productos_comprados")
    total = models.FloatField(default=0)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'boleta_compra'
        verbose_name = 'boleta de compra'
        verbose_name_plural = 'boletas de compra'
    
    def remover_alamacenes(self):
        for almacen in self.detalles.all():
            detalle = DetalleCompra.objects.get(boleta=self, almacen=almacen)
            almacen.restar_almacen(tmp.detalle)

    def delete(self, *args, **kwargs):
        self.remover_alamacenes()
        super().delete(*args, **kwargs)



class DetalleCompra(models.Model):
    boleta = models.ForeignKey(
        BoletaCompra, related_name="detalle_de_boleta", on_delete=models.CASCADE)
    almacen = models.ForeignKey(
        Almacen, related_name="producto_almacen", on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.FloatField(default=0)
    total = models.FloatField(default=0)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'detalle_compra'
        verbose_name = 'detalle de compra'
        verbose_name_plural = 'detalles de compra'
