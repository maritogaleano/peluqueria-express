from compras.models import BoletaCompra,Proveedor,DetalleCompra,Almacen

def saveBoletaFromRequest(boleta,data):
    proveedor = Proveedor.objects.get(pk=data["proveedor"])
    boleta.proveedor = proveedor
    boleta.save()
    setItemsFromBoleta(boleta,data)

def setItemsFromBoleta(boleta,data):
    detail_data = {}
    count = len(data.getlist("almacen-id"))
    total = 0
    for x in range(count):
        detail_data["pk"] = data.getlist("almacen-id")[x]
        detail_data["cantidad"] = data.getlist("cantidad")[x]
        detail_data["precio_unitario"] = data.getlist("precio_unitario")[x]
        detail_data["total"] = data.getlist("total-producto")[x]
        # detail_data["precio_unitario"] = float(data.getlist("almacen-id")[x])
        # detail_data["total"] = round( float(data["cantidad"]) * float(data["precio_unitario"]),2)
        # total = total + detail_data["total"]
        saveDetalle(detail_data,boleta)
    # recalculateTaxAndTotal(boleta,total)

def saveDetalle(data,boleta):
    item = Almacen.objects.get(pk=data["pk"])
    detail_tmp = DetalleCompra()
    detail_tmp.boleta = boleta
    detail_tmp.almacen = item
    detail_tmp.cantidad = data["cantidad"]
    detail_tmp.precio_unitario = data["precio_unitario"]
    detail_tmp.total = data["total"]
    detail_tmp.save()
    #add count items in store
    item.cantidad = int(item.cantidad) + int(detail_tmp.cantidad) 
    item.save()

def recalculateTaxAndTotal(boleta,total):
    sub_total = total
    iva = round((10/100)*total,2)
    total =  round(sub_total+iva,2)
    boleta.sub_total = sub_total
    boleta.impuesto_total  = iva
    boleta.total = total
    boleta.save()