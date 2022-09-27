from django.contrib import admin
from .models import *

class ProductoAdmin(admin.ModelAdmin):
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

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin )

admin.site.register(Categoria)
