from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin


class ProductoAdmin(ExportActionMixin, admin.ModelAdmin):
    search_fields = ['nombre','categoria', 'talla', 'marca']
    list_display = ['nombre', 'marca', 'categoria', 'talla','precio', 'stock', 'descripcion', 'fecha_ingreso', 'estado']
    list_filter = ['categoria', 'marca', 'talla' , 'precio', 'estado']


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

class dVentasInline(ExportActionMixin, admin.TabularInline):
    model = DetalleVenta
    extra = 0

class VentaResource(resources.ModelResource):
    class Meta:
        model = Venta
        fields = ('id' 'nitcliente','empleado', 'total' 'fecha_venta')

class VentaAdmin(ExportActionMixin, admin.ModelAdmin):
    inlines = [dVentasInline]
    search_fields = ['fecha_venta', 'empleado', 'nitcliente']
    list_display = ['id', 'nitcliente', 'empleado', 'fecha_venta', 'total']
    list_filter = ['fecha_venta', 'empleado', 'nitcliente']
    date_hierarchy = 'fecha_venta' #ordernar por fecha

    fieldsets = [
        ('Datos de venta', {
            'fields': (
                ('nitcliente', 'empleado'),
                ('total')
                )
        }),
    ]

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin )
admin.site.register(Categoria)
admin.site.register(Venta, VentaAdmin)
