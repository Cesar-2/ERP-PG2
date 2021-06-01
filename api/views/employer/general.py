""" Contains Employer endpoint definition """
from cerberus import Validator
from datetime import datetime

from ...serializers.employer import EmployerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models.employer import Employer
from ...models.enterprise import Enterprise

from ...helpers.paginator import paginate_content
from ...helpers.token import TokenHandler
from ...helpers.modules_names import PAYROLL_MODULE, EMPLOYER_MODULE


class EmployerApi(APIView, TokenHandler):
    """ Defines the HTTP verbs to employer model management. """

    def post(self, request):
        """ Create employer instance.

        Parameters
        ----------

        request (dict)
            Contains http transaction information.

        Returns
        -------
            Response (JSON, int)
                Body response and status code.

        """
        def to_date(s): return datetime.strptime(s, '%Y-%m-%d')
        validator = Validator({
            "name": {"required": True, "type": "string"},
            "last_name": {"required": True, "type": "string"},
            "initiation_date": {"required": True, "type": "date", "coerce": to_date},
            "birthdate": {"required": True, "type": "date", "coerce": to_date},
            "document": {"required": True, "type": "string"},
            "email": {"required": True, "type": "string"},
            "cellphone": {"required": True, "type": "string"},
            "work_from_home": {"required": False, "type": "boolean"},
            "job_tittle": {"required": True, "type": "string"},
            "address": {"required": True, "type": "string"},
            "state": {"required": True, "type": "string"},
            "city": {"required": True, "type": "string"},
            "eps": {"required": True, "type": "string"},
            "password": {"required": True, "type": "string", "minlength": 7},
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

        if not self.has_permissions([PAYROLL_MODULE], enterprise):
            return Response({
                "code": "invalid_request",
                "detailed": "No tiene los permisos necesarios"
            }, status=status.HTTP_403_FORBIDDEN)

        # request.data["enterprise"] = enterprise
        serializer = EmployerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'code': 'invalid_body',
                'detailed': 'Cuerpo de la petición con estructura inválida',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        employer = serializer.create(request.data)

        return Response({
            "inserted": employer.pk,
        }, status=status.HTTP_201_CREATED)

    @paginate_content()
    def get(self, request):
        payload, enterprise = self.get_payload(request)
        if not payload:
            return Response({
                "code": "unauthorized",
                "detailed": "El token es incorrecto o expiro"
            }, status=status.HTTP_401_UNAUTHORIZED)

        if not self.has_permissions([EMPLOYER_MODULE], enterprise):
            return Response({
                "code": "invalid_request",
                "detailed": "No tiene los permisos necesarios"
            }, status=status.HTTP_403_FORBIDDEN)

        employer = Employer.objects.filter(
            enterprise=enterprise.pk).order_by("-name")

        return Response({
            "count": employer.count(),
            "results": EmployerSerializer(
                employer[self.pagination_start:
                         self.pagination_end + 1], many=True).data
        }, status=status.HTTP_200_OK)
