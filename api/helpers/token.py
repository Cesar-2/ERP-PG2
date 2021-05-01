""" Handler for tokens """
import datetime as dt
import jwt

from django.conf import settings

from ..models.enterprise.auth import Auth
from ..models.enterprise import Enterprise
from api.models import enterprise


class TokenHandler:
    """ Controls all the token functionalities for sessions """

    def get_payload(self, request):
        """ Returns token payload if is enabled or active.

        Parameter
        ---------

        request: dict
            Request information

        Return
        ------

        dict - Token if it is active or enabled, else None

        """
        # pylint: disable=no-self-use
        header = request.headers.get("Authorization", None)
        if (not header or len(header.split(" ")) != 2 or
                header.split(" ")[0].lower() != "bearer"):
            return None, None

        try:
            token = jwt.decode(header.split(
                " ")[1], settings.SECRET_KEY, algorithms='HS256')
        except jwt.InvalidTokenError:
            return None, None

        expiration_date = dt.datetime.strptime(token['expiration_date'],
                                               '%Y-%m-%d %H:%M:%S.%f')

        db_token = Auth.objects.filter(token=header.split(" ")[1]).first()

        if (expiration_date < dt.datetime.now() or not db_token or
                db_token.is_disabled):
            return None, None

        enterprise = Enterprise.objects.filter(
            email=token["email"], is_active=True).first()

        if not enterprise:
            return None, None

        return token, enterprise

    def is_owner(self, token_email, request_child):
        """ Asserts if token owner is also the request child.

        Parameters
        ----------

        token_email: str
            Email value inside token

        request_child: str
            Request child to be asserted

        Return
        ------

        bool - True if data is the same

        """
        # pylint: disable=no-self-use
        return token_email == request_child

    def has_permissions(self, modules, enterprise):
        return enterprise.profile.filter(profile__in=modules).exists()
