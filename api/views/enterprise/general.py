""" Contains User endpoint definition """
from cerberus import Validator
from datetime import datetime

from django.db.models import Q
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...helpers import (
    ASSESSMENT_MODULE, PAYROLL_MODULE, EMPLOYER_MODULE, REPORT_MODULE,
    TokenHandler, paginate_content
)
from ...serializers import EnterpriseSerializer
from ...models import Enterprise


class EnterpriseApi(APIView, TokenHandler):
    """ Defines the HTTP verbs to enterprise model management. """

    def post(self, request):
        """ Create enterprise instance.

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
            "nit": {"required": True, "type": "string"},
            "name": {"required": True, "type": "string"},
            "email": {"required": True, "type": "string"},
            "address": {"required": True, "type": "string"},
            "state": {"required": True, "type": "string"},
            "city": {"required": True, "type": "string"},
            "password": {"required": True, "type": "string", "minlength": 7},
            "module": {
                "required": True, "type": "list", "allowed": [
                    ASSESSMENT_MODULE, PAYROLL_MODULE, EMPLOYER_MODULE, REPORT_MODULE]},
        })
        if not validator.validate(request.data):
            return Response({
                "code": "invalid_filtering_params",
                "detailed": "Parámetros de búsqueda inválidos",
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = EnterpriseSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'code': 'invalid_body',
                'detailed': 'Cuerpo de la petición con estructura inválida',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        enterprise = Enterprise.objects.filter(
            Q(email=request.data['email']) |
            Q(nit=request.data['nit'])
        ).first()

        if enterprise:
            return Response({
                "code": "user_already_exist",
                "detailed": "El usuario ya existe en la base de datos"
            }, status=status.HTTP_409_CONFLICT)

        enterprise = serializer.create(request.data)

        return Response({
            "inserted": enterprise.pk,
        }, status=status.HTTP_201_CREATED)
