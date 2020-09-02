from django import forms
from .models import BoletaCompra

class BoletaForm(forms.ModelForm):
    class Meta:
        model = BoletaCompra
        fields = ('__all__')
        exclude = ('detalles','proveedor')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_compra'].widget = forms.DateInput(attrs={'class': 'form-control','autocomplete': 'off','type':'date'});
    
        self.fields['facturado'].widget.attrs.update({'class': 'form-control','onclick':'displayDiv(checked)'})

        self.fields['fecha_facturado'].widget = forms.DateInput(attrs={'class': 'form-control','autocomplete': 'off','type':'date'});
        self.fields['fecha_facturado'].required = False
        self.fields['numero_factura'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero_factura'].required = False
    
        self.fields['sub_total'].widget.attrs.update({'class': 'form-control','readonly':'readonly'})
        self.fields['impuesto_total'].widget.attrs.update({'class': 'form-control','readonly':'readonly'})
        self.fields['total'].widget.attrs.update({'class': 'form-control','readonly':'readonly'})
        self.fields['comentarios'].widget.attrs.update({'class': 'form-control'})