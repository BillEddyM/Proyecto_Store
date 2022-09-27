from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre= models.CharField('nombre', max_length=35, unique=True)
    descripcion = models.TextField('descripcion', max_length=255)
    precio = models.DecimalField('precio', max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField('stock')
    fecha_ingreso = models.DateField('fecha de ingreso')
    estado = models.BooleanField('disponible', default=True)

    def save(self, **kwargs):
        if self.stock == 0:
            self.estado = False
            super(Producto,self).save()
        else:
            self.estado = True
            super(Producto, self).save()
        super(Producto,self).save()

    class Meta():
        db_table = 'Producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return "%s | Q %s | Stock: %s" % (self.nombre_producto, self.precio, self.stock)