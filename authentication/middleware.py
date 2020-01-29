from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print(dir(request))

        user = User()

        return user, None