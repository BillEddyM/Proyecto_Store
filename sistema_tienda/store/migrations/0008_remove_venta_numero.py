# Generated by Django 4.0 on 2022-10-04 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_venta_detalleventa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='numero',
        ),
    ]
