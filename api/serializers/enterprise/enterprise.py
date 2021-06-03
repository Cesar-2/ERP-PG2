""" Contains Enterprise serializer definition """
import copy
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ...models.enterprise.module import Module
from ...serializers.enterprise.module import ModuleSerializer
from ...services.Enterprise_register import EnterpriseModules

USER = get_user_model()


class EnterpriseSerializer(serializers.ModelSerializer):
    """ Defines enterprise serializer behaviour. """
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=USER.objects.all())]
    )
    module = ModuleSerializer(read_only=True, many=True, required=False)
    nit = serializers.CharField(
        validators=[UniqueValidator(queryset=USER.objects.all())])

    class Meta:
        """ Defines serializer fields that are being used """

        model = USER
        fields = [
            'pk', 'email', 'name', 'state', 'city', 'address',
            'nit', 'module', 'creation_date'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Creates an entreprise object with its password and relate it with
            its modules.

        Parameters:
            validated_data (dict):Contains the data from enterprise that is going to
                                  be created.

        Returns:
            enterprise (Enterprise): A fields-full custom django enterprise.

        """
        aux = copy.deepcopy(validated_data)
        aux['username'] = aux['email'].lower()
        aux['email'] = aux['email'].lower()
        aux['password'] = make_password(validated_data['password'])
        modules = aux['module'].copy()
        aux.pop('module')
        enterprise = USER.objects.create(**aux)
        for module in modules:
            enterprise = EnterpriseModules(enterprise).add_module(module)
        enterprise.save()

        return enterprise


class BasicEnterpriseSerializer(serializers.ModelSerializer):
    """ Defines enterprise serializer behaviour. """
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=USER.objects.all())]
    )
    nit = serializers.CharField(
        validators=[UniqueValidator(queryset=USER.objects.all())])

    class Meta:
        """ Defines serializer fields that are being used """

        model = USER
        fields = [
            'pk', 'email', 'name', 'nit'
        ]
