""" Contains the TypeAssessment model"""

from django.db import models
from ...models.enterprise import Enterprise


class TypeAssessment(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    type = models.CharField("Tipos de evaluacion", max_length=255)

    class Meta:
        """ Sets human readable name """
        verbose_name = "Tipo de evaluacion"
        verbose_name_plural = "Tipos de evaluaciones"

    def __str__(self):
        return f"{self.pk} - {self.enterprise}"
