from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin

from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from import_export.resources import ModelResource


#  ____________________ ADMIN PRODUCTO ____________________________________

class ProductoResource(ModelResource):

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'marca__marca', 'categoria', 'talla','precio', 'stock', 'descripcion', 'fecha_ingreso']

class ProductoAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ['nombre','categoria', 'talla', 'marca']
    list_display = ['nombre', 'marca', 'categoria', 'talla','precio', 'stock', 'descripcion', 'fecha_ingreso', 'estado']
    list_filter = ['categoria', 'marca', 'talla' , 'precio', 'estado']
    resource_classes = [ProductoResource]

    fieldsets = [
        ('Datos del Producto', {
            'fields': (
                ('nombre', 'categoria'),
                ('descripcion'),
                ('marca', 'talla',),
                ('precio', 'stock',),
                ('fecha_ingreso'), 
                ('estado')
                )
        }),
    ]

#___________________________ ADMIN   VENTAS  ____________________________
class dVentasInline(ExportActionMixin, admin.TabularInline):
    model = DetalleVenta
    extra = 0

class VentaAdmin(ExportActionMixin, admin.ModelAdmin):
    inlines = [dVentasInline]
    search_fields = ['fecha_venta', 'empleado', 'nitcliente', 'nombre_cliente']
    list_display = ['id', 'nitcliente', 'nombre_cliente', 'empleado', 'fecha_venta', 'total']
    list_filter = ['fecha_venta', 'empleado', 'nitcliente']
    date_hierarchy = 'fecha_venta' #ordernar por fecha
    readonly_fields = ['total']

    fieldsets = [
        ('Datos de venta', {
            'fields': (
                ('nitcliente', 'nombre_cliente'),
                ('empleado'),
                ('total')
                )
        }),
    ]

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin )
admin.site.register(Categoria)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Talla)
