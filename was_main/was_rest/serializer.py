from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk', 'user')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ('pk', 'user', 'score', 'create_time')
