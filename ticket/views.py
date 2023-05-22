from rest_framework import generics, permissions, response, status

from ticket import models, serializers, filters
from ticket import permissions as ticket_permissions


class TicketCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.TicketSerializer
    queryset = models.Ticket.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_duplicate_ticket(queryset=self.queryset, user=self.request.user, data=request.data):
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer: serializer_class):
        serializer.save(request=self.request)


class TicketListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ticket_permissions.IsOwner, ]
    serializer_class = serializers.TicketSerializer
    queryset = models.Ticket.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class OccupiedSeatsAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = serializers.OccupiedSeatsSerializer
    filter_backends = [filters.TicketFilter, ]
    filterset_fields = ['session_id']
    queryset = models.Ticket.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class TicketRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ticket_permissions.IsOwner, ]
    serializer_class = serializers.TicketSerializer
    queryset = models.Ticket.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
