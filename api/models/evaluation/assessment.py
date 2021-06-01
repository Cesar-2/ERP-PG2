""" Contains the Assessment model"""

from django.db import models
from ...models.employer import Employer
from ...models.enterprise import Enterprise


class Assessment(models.Model):
    """ Assessment model """
    type = models.CharField("Clase de evaluacion", max_length=255)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    evaluator = models.ForeignKey(Employer, on_delete=models.CASCADE)
    qualification = models.IntegerField("Calificacion")
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        """ Sets human readable name """
        verbose_name = "Evaluacion"
        verbose_name_plural = "Evaluaciones"

    def __str__(self):
        return f"{self.pk} - {self.employer} {self.evaluator} : {self.qualification}"
