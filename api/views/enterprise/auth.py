""" Contains Auth endpoint definition"""
from cerberus import Validator
from django.conf import settings

import datetime as dt
import jwt

from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils.crypto import get_random_string
from django.utils import timezone

from ...models.enterprise import Enterprise, Auth


class AuthApi(APIView):
    """ Defines the HTTP verb to auth model management """

    def post(self, request):
        """ Creates a new session.

        Parameters
        -----------

        request (dict)
            Contains https transaction information.

        Returns
        -------
            Response(int)
                Response status code.
        """
        validator = Validator({
            "email": {"required": True, "type": "string"},
            "password": {"required": True, "type": "string", "minlength": 7},
            "keep_logged_in": {"required": True, "type": "boolean"}
        })
        if not validator.validate(request.data):
            return Response({
                "code": "invalid_filtering_params",
                "detailed": "Parámetros de búsqueda inválidos",
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        enterprise = Enterprise.objects.filter(
            email=request.data["email"]
        ).first()

        if not enterprise:
            return Response({
                "code": "enterprise_not_found",
                "detailed": "Empresa no encontrada"
            }, status=status.HTTP_404_NOT_FOUND)

        if not check_password(request.data["password"], enterprise.password):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        refresh = get_random_string(30)

        token = jwt.encode({
            'expiration_date': str(
                (
                    dt.datetime.now() +
                    dt.timedelta(
                        days=settings.TOKEN_EXP_DAYS
                        if not request.data['keep_logged_in']
                        else settings.KEEP_LOGGED_IN_TOKEN_EXP_DAYS
                    )
                )
            ),
            'email': request.data["email"],
            'modules': [val.names for val in enterprise.module.all()],
            'refresh': refresh
        }, settings.SECRET_KEY, algorithm='HS256')

        Enterprise.objects.filter(
            email=request.data['email']
        ).update(last_login=timezone.now())
        Auth.objects.create(token=token)

        return Response({
            "token": token,
            "refresh": refresh,
            "name": enterprise.name,
            "modules": [val.names for val in enterprise.module.all()]
        }, status=status.HTTP_201_CREATED)
