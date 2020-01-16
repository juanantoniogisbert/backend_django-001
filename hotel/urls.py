from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSetAdmin, HotelViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)

urlpatterns = [
    url(r'', include(router.urls)),

]
