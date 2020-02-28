from django.db import models

# Create your models here.
class Hospital(models.Model):
    identificacion = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=255, default="")
    telefono = models.CharField(max_length=100, default="")
    nombre = models.CharField(max_length=255, default="")
    direccion = models.CharField(max_length=255, default="")
    servicios_ofrecidos_hospital = models.CharField(max_length=255, default="")

class Medico(models.Model):
    identificacion = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=255, default="")
    telefono = models.CharField(max_length=100, default="")
    nombre = models.CharField(max_length=255, default="")
    direccion = models.CharField(max_length=255, default="")
    observaciones_medicas = models.CharField(max_length=255, default="")
    estado_salud_paciente = models.CharField(max_length=255, default="")
    especialidad_medica_brindada = models.CharField(max_length=255, default="")

class Paciente(models.Model):
    identificacion = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=255, default="")
    telefono = models.CharField(max_length=100, default="")
    nombre = models.CharField(max_length=255, default="")
    direccion = models.CharField(max_length=255, default="")
    fecha_de_nacimiento = models.DateField(default=(2020, 1, 1))
