from django.contrib import admin
from .models import *

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre','descripcion']
    list_display = ['nombre', 'descripcion', 'precio', 'stock','fecha_ingreso', 'estado']
    list_filter = ['fecha_ingreso', 'precio', 'estado']


    fieldsets = [
        ('Datos del Producto', {
            'fields': (
                ('nombre', 'descripcion'),
                ('precio', 'stock', 'fecha_ingreso'), 
                ('estado')
                )
        }),
    ]


admin.site.register(Producto, ProductoAdmin)
