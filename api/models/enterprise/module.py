""" Contains the Profile model"""

from django.db import models


class Module(models.Model):
    """ Module model """

    names = models.CharField("Nombres de los modulos", max_length=255)

    class Meta:
        """ Sets human readable name """
        verbose_name = "Modulo"
        verbose_name_plural = "Modulos"

    def __str__(self):
        return self.names
