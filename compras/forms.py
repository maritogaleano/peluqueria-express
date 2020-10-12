from .models import BoletaCompra,Proveedor,Almacen
from django import forms

class BoletaForm(forms.ModelForm):
    class Meta:
        model = BoletaCompra
        fields = ('__all__')
        exclude = ('detalles','proveedor')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # head
        self.fields['fecha_compra'].widget = forms.DateInput(attrs={'class': 'form-control','autocomplete': 'off','type':'date'});
    
        self.fields['facturado'].widget.attrs.update({'class': 'form-control','onclick':'displayDiv(checked)'})

        # do bill data no required
        self.fields['fecha_facturado'].widget = forms.DateInput(attrs={'class': 'form-control','autocomplete': 'off','type':'date'});
        self.fields['fecha_facturado'].required = False
        self.fields['numero_factura'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero_factura'].required = False
    
        self.fields['sub_total'].widget.attrs.update({'class': 'form-control','readonly':'readonly'})
        self.fields['impuesto_total'].widget.attrs.update({'class': 'form-control','readonly':'readonly'})
        self.fields['total'].widget.attrs.update({'class': 'form-control','readonly':'readonly'})
        self.fields['comentarios'].widget.attrs.update({'class': 'form-control'})

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('nombre','ruc','direccion','telefono')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update(
            {'class': 'form-control','placeholder':'Nombre del Proveedor', 'autocomplete': 'off'})
        self.fields['ruc'].widget.attrs.update(
            {'class': 'form-control','placeholder':'RUC del Proveedor', 'autocomplete': 'off'})
        self.fields['direccion'].widget.attrs.update(
            {'class': 'form-control','placeholder':'Direccion del Proveedor', 'autocomplete': 'off'})
        self.fields['telefono'].widget.attrs.update(
            {'class': 'form-control','placeholder':'Telefono del Proveedor', 'autocomplete': 'off'})

class ProductForm(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update(
            {'class': 'form-control','placeholder':'Nombre', 'autocomplete': 'off'})
        self.fields['detalle'].widget.attrs.update(
            {'class': 'form-control','placeholder':'Descripcion del producto', 'autocomplete': 'off'})
        self.fields['precio'].widget.attrs.update(
            {'class': 'form-control','placeholder':'precio', 'autocomplete': 'off'})
        self.fields['cantidad'].widget.attrs.update(
            {'class': 'form-control','placeholder':'precio', 'autocomplete': 'off'})