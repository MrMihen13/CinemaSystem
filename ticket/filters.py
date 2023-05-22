import coreapi

from rest_framework.request import Request

from django_filters import filters, filterset
from django_filters.filters import BaseInFilter

from django.db.models import QuerySet


class TicketFilter(BaseInFilter):
    filterset_base = filterset.FilterSet

    @staticmethod
    def __filter_by_session(tickets: QuerySet, request: Request):
        if request.data.get('session_id'):
            return tickets.filter(session_id=request.data.get('session_id'))
        return tickets

    def filter_queryset(self, request, tickets, view):
        tickets = self.__filter_by_session(tickets, request)
        return tickets

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
