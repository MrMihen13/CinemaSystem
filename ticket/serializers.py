from django.db.models import QuerySet

from rest_framework import serializers
from rest_framework.request import Request

from ticket import models as ticket_models
from ticket.exceptions import DuplicateTicketError
from session import serializers as session_serializer
from session import models as session_models


class TicketSerializer(serializers.ModelSerializer):
    session = session_serializer.SessionSerializer(read_only=True)
    price = session_serializer.PriceListSerializer(read_only=True)
    session_id = serializers.IntegerField(write_only=True)
    price_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ticket_models.Ticket
        fields = ['id', 'row', 'seat', 'session', 'price', 'session_id', 'price_id']

    @staticmethod
    def is_duplicate_ticket(queryset: QuerySet, user, data) -> bool:
        print(data)
        if not queryset.filter(user=user, session=data.get('session'), row=data.get('row'),
                               seat=data.get('seat')).exists():
            return True
        raise DuplicateTicketError

    def save(self, request: Request, **kwargs):
        validated_data = {**self.validated_data, **kwargs}

        validated_data.update(
            user=request.user,
            session=session_models.Session.objects.filter(id=validated_data.pop('session_id')).first(),
            price=session_models.PriceList.objects.filter(id=validated_data.pop('price_id')).first()
        )

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)

        return self.instance


class OccupiedSeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket_models.Ticket
        fields = ['row', 'seat', ]
