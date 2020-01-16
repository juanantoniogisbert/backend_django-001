from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import (ClientViewSetAdmin, ClientViewSet, ClientViewList)


router = DefaultRouter()
router.register(r'clients', ClientViewSet)

# Admin
router.register(r'clients_Admin', ClientViewSetAdmin)

urlpatterns = [
    url(r'', include(router.urls)),
    # url(r'^clientlist/?$', ClientViewList.as_view()),
]
