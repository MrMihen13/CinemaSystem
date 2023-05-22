import coreapi

from django_filters import filters, filterset
from django_filters.filters import BaseInFilter

from django.db.models import QuerySet


class SessionFilter(BaseInFilter):
    filterset_base = filterset.FilterSet

    @staticmethod
    def __filtering_by_date(session: QuerySet, datetime_to: str = None, datetime_from: str = None):
        if datetime_to:
            session = session.filter(start_time__lte=datetime_to)

        if datetime_from:
            session = session.filter(start_time__gte=datetime_from)

        return session

    @staticmethod
    def __filtering_by_price(session: QuerySet, price_to=None, price_from=None):
        if price_to:
            session = session.filter(price__price__lte=price_to)

        if price_from:
            session = session.filter(price__price__gte=price_from)

        return session

    @staticmethod
    def __filtering_by_movie(session: QuerySet, move_id: int = None):
        if move_id:
            return session.filter(move__id=move_id)
        return session

    @staticmethod
    def __filtering_by_cinema(session: QuerySet, cinema_id: int = None):
        if cinema_id:
            return session.filter(cinema__id=cinema_id)
        return session

    def filter_queryset(self, request, session, view):
        session = self.__filtering_by_date(
            session=session,
            datetime_from=request.GET.get('datetime_from'),
            datetime_to=request.GET.get('datetime_to')
        )
        session = self.__filtering_by_price(
            session=session,
            price_from=request.GET.get('price_from'),
            price_to=request.GET.get('price_to')
        )
        session = self.__filtering_by_movie(session=session, move_id=request.GET.get('movie_id'))
        session = self.__filtering_by_cinema(session=session, cinema_id=request.GET.get('cinema_id'))

        return session

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
