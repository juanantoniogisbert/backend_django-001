from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Login(APIView):

    def post(self, request):
        return Response('Hola', status=status.HTTP_200_OK)
