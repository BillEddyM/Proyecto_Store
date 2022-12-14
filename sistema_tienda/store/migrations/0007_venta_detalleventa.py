# Generated by Django 4.0 on 2022-10-04 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
        ('store', '0006_alter_categoria_categoria_alter_marca_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nitcliente', models.CharField(max_length=10, verbose_name='nitcliente')),
                ('fecha_venta', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='total')),
                ('numero', models.IntegerField(verbose_name='numero')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'venta',
                'verbose_name_plural': 'ventas',
                'db_table': 'venta',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='sub_total')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.producto', verbose_name='Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.venta', verbose_name='Venta')),
            ],
            options={
                'verbose_name': 'detalle de venta',
                'verbose_name_plural': 'detalles de ventas',
                'db_table': 'venta_detalle',
            },
        ),
    ]
