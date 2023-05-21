from rest_framework import generics, permissions, response, filters

from movie import models, serializers

from movie.filters import MovieFilter


class GenreListAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.GenreSerializers
    queryset = models.Genre.objects.all()


class MovieRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.MovieSerializers
    queryset = models.Movie.objects.all()


class PopularMovieListAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.MovieSerializers
    queryset = models.Movie.objects.order_by('-rating')[:10]


class MoviesListAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.MovieSerializers
    filter_backends = [MovieFilter, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['rating_from', 'rating_to', 'duration_from', 'duration_to', 'genre']
    queryset = models.Movie.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
