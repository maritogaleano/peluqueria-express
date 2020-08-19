# Generated by Django 3.0.4 on 2020-08-06 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True, verbose_name='Nombre y Apellido')),
                ('documento', models.CharField(max_length=100, verbose_name='CI / RUC ')),
                ('fecha_nac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('telefono', models.CharField(max_length=100, verbose_name='Teléfono - Celular')),
                ('email', models.EmailField(max_length=70, verbose_name='Email')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
                ('ciudad', models.CharField(max_length=150, verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleados',
            },
        ),
        migrations.CreateModel(
            name='HistoricalEmpleado',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=150, verbose_name='Nombre y Apellido')),
                ('documento', models.CharField(max_length=100, verbose_name='CI / RUC ')),
                ('fecha_nac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('telefono', models.CharField(max_length=100, verbose_name='Teléfono - Celular')),
                ('email', models.EmailField(max_length=70, verbose_name='Email')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
                ('ciudad', models.CharField(max_length=150, verbose_name='Ciudad')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Empleado',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
