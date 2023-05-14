from rest_framework import generics, permissions, response

from django_filters.rest_framework import DjangoFilterBackend

from session.serializers import SessionSerializer
from session.models import Session
from session.filters import SessionFilter


class ListSessionAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SessionSerializer
    filter_backends = [SessionFilter, ]
    filterset_fields = ['datetime_from', 'datetime_to', 'price_from', 'price_to']
    queryset = Session.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
