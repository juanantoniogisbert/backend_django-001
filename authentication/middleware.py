import jwt
from rest_framework import authentication
from rest_framework import exceptions

from authentication.models import User
from djangobackend import settings


class CustomAuthentication(authentication.BaseAuthentication):
    TOKEN_HEADER = 'Token'

    def authenticate(self, request):
        authorization = request.META.get('HTTP_AUTHORIZATION', None)

        if not authorization:
            return None

        splittedAuth = authorization.split()

        if len(splittedAuth) != 2:
            return None

        if splittedAuth[0] != self.TOKEN_HEADER:
            return None

        token = splittedAuth[1]

        return self.authenticate_credentials(request, token)

    def authenticate_credentials(self, request, token):
        """
        Try to authenticate the given credentials. If authentication is
        successful, return the user and token. If not, throw an error.
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            # except ValueError:
            #     print(ValueError)
            msg = 'Invalid authentication. Could not decode token.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)

        return user, token
