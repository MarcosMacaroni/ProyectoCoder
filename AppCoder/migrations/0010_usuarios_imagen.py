# Generated by Django 3.2.9 on 2021-12-25 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0009_auto_20211223_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios'),
        ),
    ]
