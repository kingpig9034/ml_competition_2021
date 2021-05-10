from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from .viewsets import *

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewset)
router.register(r'scores', ScoreViewset)

app_name = 'api'
urlpatterns = [
    url(r'^', include(router.urls), ),
    url(r'^api-auth/', include('rest_framework.urls', namespace='api')),

]