from .models import *
from rest_framework import serializers

class team_serializer(serializers.ModelSerializer):
    class Meta:
        model = team_model
        fields = '__all__'
        depth =1

class room_serializer(serializers.ModelSerializer):
    class Meta:
        model = room_model
        fields = '__all__'

class timing_serializer(serializers.ModelSerializer):
    class Meta:
        model = timing_model
        fields = '__all__'