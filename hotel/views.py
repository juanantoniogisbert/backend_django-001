
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from hotel import models
from hotel.models import Comment
from hotel.serializers import HotelSerializer, CommentSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = HotelSerializer


# Admin
class HotelViewSetAdmin(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = (IsAuthenticated,)
    permission_classes = (IsAdminUser,)

class CommentViewSetAdmin(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    permission_classes = (IsAdminUser,)
