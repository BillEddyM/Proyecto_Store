# Generated by Django 4.0.4 on 2022-05-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTelefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='tipo telefono')),
            ],
            options={
                'verbose_name': 'Tipo Telefono',
                'verbose_name_plural': 'Tipos de Telefonos',
                'db_table': 'tipo_telefono',
            },
        ),
    ]