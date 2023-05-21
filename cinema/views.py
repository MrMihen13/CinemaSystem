from rest_framework import generics, permissions

from cinema import serializers, models, filters


class CinemaRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.CinemaSerializer
    queryset = models.Cinema.objects.all()


class CinemaListAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.CinemaSerializer
    filter_backends = [filters.CinemaFilter, ]
    filterset_fields = ['movie_id']
    queryset = models.Cinema.objects.all()
