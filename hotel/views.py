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

    def create(self, request, hotel_id=None):
        data = request.data.get('comment', {})
        context = {'author': request.user.profile}

        try:
            context['post'] = Post.objects.get(slug=post_slug)
        except Post.DoesNotExist:
            raise NotFound('An post with this slug does not exist.')
            
        serializer = self.serializer_class(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
