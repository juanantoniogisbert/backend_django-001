# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from clients import models
from clients.serializers import ClientSerializer


class ClientViewSetAdmin(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
    permission_classes = (IsAdminUser,)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = (IsAuthenticated,)


class ClientViewList(ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = ClientSerializer

