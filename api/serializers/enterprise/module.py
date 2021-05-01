""" Contains Module serializer definition """

from rest_framework import serializers
from ...models.enterprise.module import Module


class ModuleSerializer(serializers.ModelSerializer):
    """ Defines model serializer behaviour. """
    class Meta:  # pylint: disable=too-few-public-methods
        """ Defines serializer fields that are being used """

        model = Module
        fields = ['names']
