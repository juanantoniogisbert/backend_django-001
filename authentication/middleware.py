from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


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

        # COMPROBAR LOGIN
        print(token)

        user = User()

        return user, None