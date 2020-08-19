from .models import Servicio
from django import forms
from django.forms import ModelForm

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

        widgets = {
            
            'nombre': forms.TextInput(
                attrs={
                    'autocomplete': 'off',
                    'placeholder': 'Nombre del Servicio'
            
                },
            ),

            'precio': forms.TextInput(
                attrs={
                    'autocomplete': 'off',
                    'placeholder': 'Precio del servicio'
                },
            ),
    }