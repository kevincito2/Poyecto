from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


class Region(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    rut = models.CharField(max_length=12)
    nombre_completo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=12,null=True)
    email = models.EmailField()
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    tipo_vivienda_choices = (
                     ('PATIO_GRANDE','Casa con patio grande'),
                     ('PATIO_PEQUEÑO','Casa con patio pequeño'),
                     ('SIN_PATIO','Casa sin patio'),
                     ('DEPTO','Departamento'),
    )
    tipo_vivienda = models.CharField(max_length=30,choices=tipo_vivienda_choices,default='RESCATADO')
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.rut

    class Meta:
        permissions = (
            ('usuario', _('Usuario')),
        )  


class Mascotas(models.Model):
    foto = models.ImageField(blank=True,null=True,upload_to="perro/%Y")
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    estado_choices = (
                     ('RESCATADO','Rescatado'),
                     ('DISPONIBLE','Disponible'),
                     ('ADOPTADO','Adoptado'),
    )
    estado = models.CharField(max_length=15,choices=estado_choices,default='RESCATADO')

    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = (
            ('mantenedor_mascotas', _('Mascotas')),
        )  



# Create your models here.
