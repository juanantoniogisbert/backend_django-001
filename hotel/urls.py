from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSetAdmin, HotelViewSet, CommentViewSetAdmin

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'comments_Admin', CommentViewSetAdmin)

urlpatterns = [
    url(r'', include(router.urls)),

]
