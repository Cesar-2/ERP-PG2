""" Contains the job_tittle model"""


from django.db import models
from ..enterprise import Enterprise


class JobTittle(models.Model):
    """ Job tittle model """
    position = models.CharField("Nombre del cargo", max_length=255)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.position}"
