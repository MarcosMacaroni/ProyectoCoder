# Generated by Django 3.2.9 on 2022-01-12 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0011_avatarusuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='imagen',
        ),
        migrations.DeleteModel(
            name='AvatarUsuario',
        ),
    ]