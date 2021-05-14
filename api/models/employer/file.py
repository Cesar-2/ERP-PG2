""" Contains the Document model"""


from .employer import Employer
from django.db import models


class File(models.Model):
    """ Document model """
    document_name = models.CharField("Nombre del documento", max_length=255)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    files = models.BinaryField("Archivo")

    def __str__(self):
        return self.pk
