from rest_framework import generics, permissions

from ticket import models, serializers
from ticket import permissions as ticket_permissions


class TicketCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.TicketSerializer
    queryset = models.Ticket.objects.all()


class TicketListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ticket_permissions.IsOwner, ]
    serializer_class = serializers.TicketSerializer
    queryset = models.Ticket.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TicketRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ticket_permissions.IsOwner, ]
    serializer_class = serializers.TicketSerializer
    queryset = models.Ticket.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
