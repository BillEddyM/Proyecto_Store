# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
# Create your models here.
GENDER_CHOISES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

class Persona(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    apellido = models.CharField('apellido', max_length=50)

    genero = models.CharField('genero', max_length=1, choices=GENDER_CHOISES, default='M')
    fecha_nacimiento = models.DateField('fecha nacimiento')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

    def edad(self):
        years = int(
            (datetime.now().date() - self.fecha_nacimiento)
            .days / 365.25)
        return '%s años' % years

    def save(self, **kwargs):
        if self.estado:
            self.nombre = self.nombre.upper()
            self.apellido = self.apellido.upper()
        else:
            self.nombre = self.nombre.lower()
            self.apellido = self.apellido.lower()
        super(Persona, self).save()

    class Meta():
        abstract = True

class TipoTelefono(models.Model):
    tipo = models.CharField('tipo telefono', max_length=50)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'tipo_telefono'
        verbose_name = 'Tipo Telefono'
        verbose_name_plural = 'Tipos de Telefonos'
