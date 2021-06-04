""" Contains the job_tittle model"""


from django.db import models
from ..enterprise import Enterprise


class JobTittle(models.Model):
    """ Job tittle model """
    position = models.CharField(
        "Nombre del cargo", max_length=255, null=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

    class Meta:
        """ Sets human readable name """
        verbose_name = "Nombre del puesto"
        verbose_name_plural = "Nombre de los puestos"

    def __str__(self):
        return f"{self.pk} - {self.position}"
