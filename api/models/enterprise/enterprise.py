""" Contains the User model """

from django.db import models
from django.contrib.auth.models import AbstractUser
from .module import Module


class Enterprise(AbstractUser):
    """
    Extends native django user model adding new features to enterprise definition.
    """

    creation_date = models.DateTimeField(auto_now_add=True)
    nit = models.CharField("Nit de la empresa", max_length=255, unique=True)
    name = models.CharField("Nombre", max_length=255)
    state = models.CharField("Departamento", max_length=100, blank=True)
    city = models.CharField("Ciudad", max_length=100, blank=True)
    address = models.CharField("Direccion", max_length=100, blank=True)
    module = models.ManyToManyField(Module, related_name='enterprise_module')

    REQUIRED_FIELDS = ['email']

    class Meta:  # pylint: disable=too-few-public-methods
        """ Sets human readable name """
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return '{} - {} {}'.format(self.pk, self.email, self.nit)
