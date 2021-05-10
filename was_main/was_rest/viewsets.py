from rest_framework import serializers, viewsets, status, generics, filters
from rest_framework.response import Response
from django.http import HttpResponse
from .models import *
from .serializer import *

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            #
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ScoreViewset(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            #
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)
