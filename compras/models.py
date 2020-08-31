from django.db import models

# Create your models here.
# made with love by c4-technologies


class Almacen(models.Model):
    nombre = models.CharField(max_length=25, default=None, null=False)
    detalle = models.TextField(default="")
    precio = models.FloatField(default=0)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return str(self.pk)+":"+self.nombre

    class Meta:
        db_table = 'almacen'
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, default=None, null=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class BoletaCompra(models.Model):
    fecha_compra = models.DateField(default=None, null=False)
    numero_factura = models.CharField(default="0", null=True,max_length=25)
    fecha_facturado = models.DateField(default=None, null=False)
    facturado = models.BooleanField(default=False)
    proveedor = models.ForeignKey(
        Proveedor, related_name="compra_a_proveedor", on_delete=models.CASCADE)
    sub_total = models.FloatField(default=0)
    # impuesto en 10%
    impuesto_total = models.FloatField(default=0)
    Comentarios = models.TextField(default="")
    # detalle
    detalles = models.ManyToManyField(Almacen,through="DetalleCompra",related_name="productos_comprados")
    total = models.FloatField(default=0)

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'boleta_compra'
        verbose_name = 'boleta de compra'
        verbose_name_plural = 'boletas de compra'

class DetalleCompra(models.Model):
    boleta = models.ForeignKey(BoletaCompra,related_name="detalle_de_boleta",on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen,related_name="producto_almacen",on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.FloatField(default=0)
    total =  models.FloatField(default=0)

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        db_table = 'detalle_compra'
        verbose_name = 'detalle de compra'
        verbose_name_plural = 'detalles de compra'