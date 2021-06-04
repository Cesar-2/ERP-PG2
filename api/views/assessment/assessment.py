""" Contains Assessment endpoint definition """
from cerberus import Validator
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...serializers.assessment import AssessmentSerializer

from ...models.evaluation import Assessment

from ...helpers.paginator import paginate_content
from ...helpers.token import TokenHandler
from ...helpers.modules_names import ASSESSMENT_MODULE


class AssessmentApi(APIView, TokenHandler):
    """ Defines the HTTP verbs to assessment model management. """

    def post(self, request):
        """ Create assessment instance.

        Parameters
        ----------

        request (dict)
            Contains http transaction information.

        Returns
        -------
            Response (JSON, int)
                Body response and status code.

        """
        validator = Validator({
            "type": {"required": True, "type": "string"},
            "employee_evaluated": {"required": True, "type": "integer"},
            "employee_evaluator": {"required": True, "type": "integer"},
            "qualification": {"required": True, "type": "integer"},
            "feedback": {"required": True, "type": "string"},
        })
        if not validator.validate(request.data):
            return Response({
                "code": "invalid_filtering_params",
                "detailed": "Parámetros de búsqueda inválidos",
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        payload, enterprise = self.get_payload(request)
        if not payload:
            return Response({
                "code": "unauthorized",
                "detailed": "El token es incorrecto o expiro"
            }, status=status.HTTP_401_UNAUTHORIZED)

        if not self.has_permissions([ASSESSMENT_MODULE], enterprise):
            return Response({
                "code": "invalid_request",
                "detailed": "No tiene los permisos necesarios"
            }, status=status.HTTP_403_FORBIDDEN)

        request.data["enterprise"] = enterprise
        serializer = AssessmentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'code': 'invalid_body',
                'detailed': 'Cuerpo de la petición con estructura inválida',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        assessment = serializer.create(request.data)

        return Response({
            "inserted": assessment.pk,
        }, status=status.HTTP_201_CREATED)

    @paginate_content()
    def get(self, request):
        """ Retrieves assessment instance.

        Parameters
        ----------

        request (dict)
            Contains http transaction information.

        Returns
        -------
            Response (JSON, int)
                Body response and status code.

        """
        payload, enterprise = self.get_payload(request)
        if not payload:
            return Response({
                "code": "unauthorized",
                "detailed": "El token es incorrecto o expiro"
            }, status=status.HTTP_401_UNAUTHORIZED)

        if not self.has_permissions([ASSESSMENT_MODULE], enterprise):
            return Response({
                "code": "invalid_request",
                "detailed": "No tiene los permisos necesarios"
            }, status=status.HTTP_403_FORBIDDEN)

        assessment = Assessment.objects.filter(enterprise=enterprise.pk)

        return Response({
            "count": assessment.count(),
            "results": AssessmentSerializer(
                assessment[self.pagination_start:
                           self.pagination_end + 1], many=True).data
        }, status=status.HTTP_200_OK)
