from .models import Empleado
from django import forms
from django.forms import ModelForm


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

        widgets = {
            
            'nombre': forms.TextInput(
                attrs={
                    'autocomplete': 'off',
                    'placeholder': 'Nombre y Apellido'
            
                },
            ),

            'documento': forms.TextInput(
                attrs={
                    'autocomplete': 'off',
                    'placeholder': 'RUC / CI'
                },
            ),

            'fecha_nac': forms.DateInput(
                attrs={
                    'class': 'form-control datetimepicker-input',
                    'id': 'fecha_nac',
                    'data-target': '#fecha_nac',
                    'data-toggle': 'datetimepicker',
                    'autocomplete': 'off'
                }
            ),

            'telefono': forms.TextInput(
                attrs={
                    'autocomplete': 'off',
                    'placeholder': 'Línea Baja / Celular'
                },
            ),

            'email': forms.EmailInput(
                attrs={
                    'autocomplete': 'off'
                
                },
            ),

            'direccion': forms.TextInput(
                attrs={
                    'autocomplete': 'off'
                },
            ),

            'ciudad': forms.TextInput(
                attrs={
                    'autocomplete': 'off'
                },
            ),
          
        }
