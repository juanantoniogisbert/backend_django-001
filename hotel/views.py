
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from hotel import models
from hotel.serializers import HotelSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = HotelSerializer


# Admin
class HotelViewSetAdmin(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = (IsAuthenticated,)
    permission_classes = (IsAdminUser,)
