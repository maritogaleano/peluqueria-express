from .models import Agenda
from cliente.models import Clientes
from empleado.models import Empleado
from django import forms
from django.forms import ModelChoiceField
from django.forms import ModelForm


class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'

        cliente_id = ModelChoiceField(queryset=Clientes.objects.all(), widget=forms.Select(attrs={
        'class': 'select2'
        }))
        empleado_id = ModelChoiceField(queryset=Empleado.objects.all(), widget=forms.Select(attrs={
        'class': 'select2'
        }))


        widgets = {

            'servicio': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width: 100%',
                    'required': True
                }
            ),

            'hora_servicio': forms.TimeInput(
                attrs={
                    'class': 'form-control datetimepicker-input',
                    'id': 'hora_servicio',
                    'data-target': '#hora_servicio',
                    'data-toggle': 'datetimepicker',
                    'autocomplete': 'off'
                }
            ),

            'observaciones': forms.TextInput(
                attrs={
                    'autocomplete': 'off',
                    'placeholder': 'Observaciones varias'
                },
            ),

            'fecha_agendada': forms.DateInput(
                attrs={
                    'class': 'form-control datetimepicker-input',
                    'id': 'fecha_agendada',
                    'data-target': '#fecha_agendada',
                    'data-toggle': 'datetimepicker',
                    'autocomplete': 'off'
                }
            ), 
        }
