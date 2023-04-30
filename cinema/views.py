from rest_framework import generics, permissions

from cinema import serializers, models


class CinemaAPIView(generics.CreateAPIView):
    permission_classes = permissions.IsAdminUser
    serializer_class = serializers.CinemaSerializer
    queryset = models.Cinema.objects.all()


class RetrieveUpdateDestroyCinemaAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = permissions.IsAdminUser
    serializer_class = serializers.CinemaSerializer
    queryset = models.Cinema.objects.all()
