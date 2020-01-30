# from django.conf.urls import url

# from .views import ProfileRetrieveAPIView, ProfileFollowAPIView

# urlpatterns = [
#     url(r'^profiles/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
#     url(r'^profiles/(?P<username>\w+)/follow/?$', 
#         ProfileFollowAPIView.as_view()),
# ]

from django.conf.urls import url
from django.urls import reverse
from .views import ProfileRetrieveAPIView, ProfileFollowAPIView, ProfileViewSet

app_name = 'profiles'

#Admin
profile_list = ProfileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
profile_detail = ProfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^profiles/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
    url(r'^profiles/(?P<username>\w+)/follow/?$', ProfileFollowAPIView.as_view()),
    
    #Admin
    url(r'^profilelist/$', profile_list, name='profile_list'),                                      
    url(r'^profiledetail/(?P<user_id>[0-9a-zA-Z_-]+)/$', profile_detail, name='profile_detail'),    
]
