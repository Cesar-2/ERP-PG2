""" Contains the Assessment model"""

from django.db import models
from ...models.employer import Employer


class Assessment(models.Model):
    """ Assessment model """
    type = models.CharField("Clase de evaluacion", max_length=255)
    employee_evaluated = models.ForeignKey(
        Employer, on_delete=models.CASCADE, related_name="assessment_employer_evaluated")
    employee_evaluator = models.ForeignKey(
        Employer, on_delete=models.CASCADE, related_name="assessment_employer_evaluator")
    qualification = models.IntegerField("Calificacion")
    creation_date = models.DateField(auto_now_add=True)
    feedback = models.CharField(
        "Retroalimentacion", max_length=1000, blank=True)

    class Meta:
        """ Sets human readable name """
        verbose_name = "Evaluacion"
        verbose_name_plural = "Evaluaciones"

    def __str__(self):
        return f"{self.pk} - {self.employee_evaluated} {self.employee_evaluator} : {self.qualification}"
