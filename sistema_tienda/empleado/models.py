from django.db import models
from comun.models import Persona, TipoTelefono

# Create your models here.
class Empleado(Persona):
    dpi = models.CharField('DPI', max_length=14, unique=True)

    class Meta():
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        unique_together = ['nombre', 'apellido']

class TelefonoEmpleado(models.Model):
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    numero = models.CharField('telefono', max_length=12)
    tipo = models.ForeignKey(
        TipoTelefono, verbose_name='Tipo Telefono', related_name='TelEmpleado', on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s %s" % (self.Empleado, self.numero)

    class Meta():
        db_table = 'telefono_empleado'
        verbose_name = 'Telefono'
        verbose_name_plural = 'Telefonos'
