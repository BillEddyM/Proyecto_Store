from django.db import models
from django.forms import ValidationError
from empleado.models import *; 
from import_export import resources
from django.utils.safestring import mark_safe
# Create your models here.

class Categoria(models.Model):
    categoria= models.CharField('nombre', max_length=35, unique=True)

    class Meta():
        db_table  = 'Categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.categoria

#_______________________________ M A R C A  _________________________________--
class Marca(models.Model):
    marca= models.CharField('nombre', max_length=35, unique=True)
    class Meta():
        db_table = 'Marca'
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.marca

class Talla(models.Model):
    talla= models.CharField('Talla', max_length=35, unique=True)

    class Meta():
        db_table = 'Talla'
        verbose_name = 'Talla'
        verbose_name_plural = 'Tallas'

    def __str__(self):
        return self.talla

class Producto(models.Model):
    nombre= models.CharField('nombre', max_length=35, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    descripcion = models.TextField('descripcion', max_length=255)
    precio= models.DecimalField('precio', max_digits=8, decimal_places=2)
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
        return "%s | Q %s | Stock: %s" % (self.nombre, self.precio, self.stock)


#____________________________________ V E N T A ___________________________________________________
class Venta(models.Model):
    nitcliente = models.CharField(verbose_name='nitcliente', max_length=10)
    nombre_cliente = models.CharField('talla', max_length=40)
    empleado = models.ForeignKey(Empleado, verbose_name='Empleado', on_delete=models.CASCADE)
    fecha_venta= models.DateTimeField(auto_now_add=True)
    total = models.DecimalField('total', max_digits=10, decimal_places=2, default=0.00)


    def __str__(self):
        return "%s %s" % (self.id, self.fecha_venta)
    
    def save(self, **kwargs):
        monto = 0
        for dp in self.detalleventa_set.all():
            monto += dp.sub_total
        self.total = monto
        super(Venta, self).save() 

    class Meta:
        db_table = 'venta'
        verbose_name = 'venta'
        verbose_name_plural = 'ventas'

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, verbose_name='Venta', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField('cantidad')
    sub_total = models.DecimalField('sub_total', max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return "%s %s" % (self.venta, self.producto)

    def clean(self):
        if self.cantidad <= self.producto.stock: #Stock cubre venta
            self.producto.stock -= self.cantidad
            self.subtotal = self.producto.precio * self.cantidad
        else:
            raise ValidationError('STOCK INSUFICIENTE')#Stock menor a peticion
    
    def save(self, **kwargs):
        self.sub_total = self.producto.precio * self.cantidad
        super(DetalleVenta, self).save()
        self.venta.save()
        self.producto.save() # actualizar stock del producto
    
    class Meta:
        db_table = 'venta_detalle'
        verbose_name ='detalle de venta'
        verbose_name_plural ='detalles de ventas'


