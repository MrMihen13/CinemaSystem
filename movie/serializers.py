from rest_framework import serializers

from movie import models


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Country
        fields = ('id', 'name', 'language')


class DirectorSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True, read_only=True)
    language = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Director
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'country', 'language')


class ActorSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True, read_only=True)
    language = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Actor
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'country', 'language')


class ProducerSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True, read_only=True)
    language = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Director
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'country', 'language')


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'


class FavoriteMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteMovie
        fields = '__all__'


class MovieSerializers(serializers.ModelSerializer):
    genre = GenreSerializers(many=True, read_only=True)
    actor = ActorSerializer(many=True, read_only=True)
    country = CountrySerializer(many=True, read_only=True)
    language = LanguageSerializer(many=True, read_only=True)
    director = DirectorSerializer(read_only=True)
    producer = ProducerSerializer(read_only=True)

    class Meta:
        model = models.Movie
        fields = (
            'id',
            'name',
            'release_date',
            'rating',
            'duration',
            'director',
            'producer',
            'genre',
            'actor',
            'country',
            'language'
        )
