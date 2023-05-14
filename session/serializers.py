from rest_framework import serializers

from session.models import Session, PriceList
from cinema.serializers import CinemaSerializer, HallSerializer
from movie.serializers import MovieSerializers


class PriceListSerializer(serializers.ModelSerializer):
    hall = HallSerializer(read_only=True)

    class Meta:
        model = PriceList
        fields = ('id', 'price', 'places', 'hall')


class SessionSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer(read_only=True)
    hall = HallSerializer(read_only=True)
    movie = MovieSerializers(read_only=True)
    price = PriceListSerializer(read_only=True, many=True)

    class Meta:
        model = Session
        fields = ('id', 'start_time', 'cinema', 'hall', 'movie', 'price')
