from api.serializers.enterprise.enterprise import EnterpriseSerializer
import copy
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ...models.employer import Employer
from django.contrib.auth.hashers import make_password


class EmployerSerializer(serializers.ModelSerializer):
    """ Defines employer serializer behaviour. """
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Employer.objects.all())]
    )
    enterprise = EnterpriseSerializer(read_only=True)

    class Meta:
        """ Defines serializer fields that are being used """
        model = Employer
        fields = ["pk", "creation_date", "name", "last_name", "initiation_date",
                  "birthdate", "document", "email", "cellphone", "work_from_home",
                  "job_tittle", "address", "state", "city", "eps", "enterprise",
                  "documents"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Creates an entreprise object with its password and relate it with
            its modules.

        Parameters:
            validated_data (dict):Contains the data from employer that is going to
                                  be created.

        Returns:
            employer (Employer): A fields-full custom django employer.

        """
        aux = copy.deepcopy(validated_data)

        aux['email'] = aux['email'].lower()
        aux['password'] = make_password(validated_data['password'])
        employer = Employer.objects.create(**aux)
        employer.save()

        return employer
