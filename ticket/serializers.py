from rest_framework import serializers

from ticket import models
from session import serializers as session_serializer


class TicketSerializer(serializers.ModelSerializer):
    session = session_serializer.SessionSerializer(write_only=True)
    price = session_serializer.PriceListSerializer(write_only=True)

    class Meta:
        model = models.Ticket
        fields = ['id', 'row', 'seat', 'session', 'price']
