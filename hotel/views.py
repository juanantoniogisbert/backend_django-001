from rest_framework import viewsets, generics, mixins, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
import logging

from hotel import models
from hotel.models import Comment, Hotel
from hotel.serializers import HotelSerializer, CommentSerializer


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


# Api
class HotelViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class CommentsListAPIView(generics.ListCreateAPIView):
    lookup_field = 'comment__hotel'
    lookup_url_kwarg = 'hotel_id'
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def filter_queryset(self, queryset):
        idToFilter = self.kwargs[self.lookup_url_kwarg]
        return queryset.filter(hotels=idToFilter)

    def create(self, request):
        serializer_context = {
            'author': request.user.profile,
            'request': request
        }

        serializer_data = request.data.get('post', {})
        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
