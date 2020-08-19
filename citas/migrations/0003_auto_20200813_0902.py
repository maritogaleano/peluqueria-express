# Generated by Django 3.0.4 on 2020-08-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
        ('citas', '0002_auto_20200813_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalagenda',
            name='servicio',
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='servicio',
        ),
        migrations.AddField(
            model_name='agenda',
            name='servicio',
            field=models.ManyToManyField(blank=True, to='servicios.Servicio', verbose_name='Servicios'),
        ),
    ]
