""" Contains the Employer model"""

from ..enterprise import Enterprise
from django.db import models


class Employer(models.Model):
    """ Employer model """

    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField("Nombre del empleado", max_length=255)
    last_name = models.CharField("Apellido del empleado", max_length=255)
    initiation_date = models.DateField("Fecha de iniciacion")
    birthdate = models.DateField("Fecha de nacimiento", blank=True, null=True)
    document = models.CharField("Documento de identidad", max_length=255)
    email = models.CharField("Correo electronico", max_length=255)
    cellphone = models.CharField("Celular", max_length=15)
    work_from_home = models.BooleanField(
        "Trabajo desde la casa", default=False)
    job_tittle = models.CharField("Nombre del cargo", max_length=255)
    address = models.CharField("Direccion", max_length=100, blank=True)
    state = models.CharField("Departamento", max_length=100, blank=True)
    city = models.CharField("Ciudad", max_length=100, blank=True)
    eps = models.CharField("EPS", max_length=255)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    password = models.CharField("Contraseña", max_length=255)

    REQUIRED_FIELDS = ['document', 'job_tittle',
                       'eps', 'initiation_date', 'enterprise']

    class Meta:
        """ Sets human readable name """
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return f"{self.pk} - {self.name} {self.email}"
