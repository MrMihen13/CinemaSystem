from rest_framework import generics, permissions

from cinema import serializers, models


class CinemaRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = serializers.CinemaSerializer
    queryset = models.Cinema.objects.all()


class CinemaListAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = serializers.CinemaSerializer
    queryset = models.Cinema.objects.all()
