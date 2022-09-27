from django.contrib import admin
from .models import *

class TipoTelefonoAdmin(admin.ModelAdmin):
    search_fields = ['tipo']

# Register your models here.
admin.site.register(TipoTelefono,TipoTelefonoAdmin)