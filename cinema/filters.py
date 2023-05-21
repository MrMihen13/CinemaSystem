import coreapi

from django_filters import filters, filterset
from django_filters.filters import BaseInFilter

from django.db.models import QuerySet

from session import models as session_models
from cinema import models as cinema_models


class CinemaFilter(BaseInFilter):
    filterset_base = filterset.FilterSet

    @staticmethod
    def __filtering_by_movie(cinemas: QuerySet[cinema_models.Cinema], movie_id: int = None):
        if movie_id:
            sessions = session_models.Session.objects.filter(movie_id=movie_id).values_list('cinema_id', flat=True)
            return cinemas.filter(id__in=sessions)
        return cinemas

    def filter_queryset(self, request, cinemas, view):
        movie_id = request.GET.get('movie_id')
        cinemas = self.__filtering_by_movie(movie_id=movie_id, cinemas=cinemas)
        return cinemas

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
