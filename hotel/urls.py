from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import HotelViewSetAdmin, CommentViewSetAdmin, HotelViewSet, CommentsListAPIView

router = DefaultRouter()
router.register(r'hotels_Admin', HotelViewSetAdmin)
router.register(r'comments_Admin', CommentViewSetAdmin)

router.register('', HotelViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url(r'^(?P<hotel_id>[0-9a-zA-Z_-]+)/comments', CommentsListAPIView.as_view()),
]
