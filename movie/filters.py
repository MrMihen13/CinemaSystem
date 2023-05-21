import coreapi

from django_filters import filters, filterset
from django_filters.filters import BaseInFilter

from django.db.models import QuerySet


class MovieFilter(BaseInFilter):
    filterset_base = filterset.FilterSet

    @staticmethod
    def __filter_movie_by_name(movie: QuerySet, name: str):
        if name:
            movie = movie.filter(name=name)

        return movie

    @staticmethod
    def __filtering_movie_by_rating(movie: QuerySet, rating_to, rating_from):
        if rating_to:
            movie = movie.filter(rating__lte=rating_to)

        if rating_from:
            movie = movie.filter(rating__gte=rating_from)

        return movie

    @staticmethod
    def __filtering_movie_by_duration(movie: QuerySet, duration_to, duration_from):
        if duration_to:
            movie = movie.filter(duration__lte=duration_to)

        if duration_from:
            movie = movie.filter(duration__gte=duration_from)

        return movie

    @staticmethod
    def __filtering_movie_by_genre(movie: QuerySet, genre):
        if genre is None:
            return movie
        genre_ids = list(map(int, genre.split(',')))
        if len(genre_ids) != 0:
            movie = movie.filter(genre__id__in=genre_ids)
        return movie

    def filter_queryset(self, request, queryset, view):
        movie = queryset

        movie = self.__filter_movie_by_name(
            movie=movie,
            name=request.GET.get('name'),
        )
        movie = self.__filtering_movie_by_rating(
            movie=movie,
            rating_from=request.GET.get('rating_from'),
            rating_to=request.GET.get('rating_to')
        )
        movie = self.__filtering_movie_by_duration(
            movie=movie,
            duration_from=request.GET.get('duration_from'),
            duration_to=request.GET.get('duration_to')
        )
        movie = self.__filtering_movie_by_genre(
            movie=movie,
            genre=request.GET.get('genre')
        )
        return movie

    @staticmethod
    def get_schema_fields(view):
        filterset_fields = getattr(view, "filterset_fields", None)
        return [
            coreapi.Field(
                name=field_name,
                required=False,
                location="query",
            )
            for field_name in filterset_fields
        ]
