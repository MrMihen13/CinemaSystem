from rest_framework import serializers

from cinema import models


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cinema
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hall
        fields = '__all__'
