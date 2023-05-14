from rest_framework import generics, permissions

from movie import models, serializers


class MoveRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.MovieSerializers
    queryset = models.Movie.objects.all()


class MoviesListAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.MovieSerializers
    queryset = models.Movie.objects.all()
