# Generated by Django 3.2.9 on 2021-12-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_rename_actividad_realizar_turnos_actividad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnos',
            name='fecha',
            field=models.DateTimeField(verbose_name='%d/%m/$y'),
        ),
    ]
