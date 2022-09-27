from django.contrib import admin
from .models import *

class TelefonoEmpleadoInline(admin.TabularInline):
    model = TelefonoEmpleado
    extra = 0
    autocomplete_fields = ['tipo'] #BUSQUEDA SOBRE EL CAMPO

class EmpleadoAdmin(admin.ModelAdmin):
    inlines = [TelefonoEmpleadoInline]
    actions = ['inactivar', 'activar'] #registro de Acciones
    search_fields = ['nombre', 'apellido']
    list_filter = ['genero', 'estado']
    list_display = ['nombre', 'dpi', 'apellido', 'genero', 'edad', 'estado']

    readonly_fields =['estado']

    fieldsets = [
        ('Datos Personales', {
            'fields': (
                ('dpi'),
                ('nombre', 'apellido'), 
                ('genero', 'fecha_nacimiento', 'estado')
                )
        }),
    ]

    def inactivar(self, request, queryset):
    
        for row in queryset.filter(estado = True):
            self.log_change(request, row, 'inactivar empleado')
            rows_updated = 0
        
        for obj in queryset:
            if obj.estado:
                obj.estado = False
                obj.save()

                rows_updated +=1

        if rows_updated == 1:
            message_bit = "1 empleado se marco"
        else:
            message_bit = "%s empleados se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactorialmente como inactivas" % message_bit)
    inactivar.short_description = 'inactivar empleado'

    def activar(self, request, queryset):

        for row in queryset.filter(estado = False):
            self.log_change(request, row, 'activar empleado')
            rows_updated = 0

        for obj in queryset:
            if obj.estado == False:
                obj.estado = True
                obj.save()

                rows_updated +=1

        if rows_updated == 1:
            message_bit = "1 empleado se marco"
        else:
            message_bit = "%s empleados se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactorialmente como activas" % message_bit)
    activar.short_description = 'activar empleado'

# Register your models here.
admin.site.register(Empleado, EmpleadoAdmin)