import copy

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ...models.evaluation import Assessment

from ...serializers.employer import EmployerSerializer
from ...serializers.enterprise import BasicEnterpriseSerializer


class AssessmentSerializer(serializers.ModelSerializer):
    """ Defines assessment serializer behaviour. """
    employee_evaluated = EmployerSerializer(read_only=True)
    employee_evaluator = EmployerSerializer(read_only=True)
    enterprise = BasicEnterpriseSerializer(read_only=True)

    class Meta:
        """ Defines serializer fields that are being used """
        model = Assessment
        fields = ["pk", "type", "employee_evaluated", "employee_evaluator",
                  "qualification", "creation_date", "feedback", "enterprise"]

    def __str__(self):
        return (
            f"{self.pk} - {self.employee_evaluated} {self.employee_evaluator} {self.qualification}")

    def create(self, validated_data):
        """ Creates an assessment object with its password and relate it with
            its modules.

        Parameters:
            validated_data (dict):Contains the data from assessment that is going to
                                  be created.

        Returns:
            assessment (Assessment): A fields-full custom django assessment.

        """
        aux = copy.deepcopy(validated_data)
        assessment = Assessment.objects.create(**aux)
        assessment.save()

        return assessment
