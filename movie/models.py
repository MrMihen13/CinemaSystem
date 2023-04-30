from django.db import models
from django.contrib.auth import get_user_model


USER = get_user_model()


class Language(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name', blank=False, null=False)
    code = models.CharField(max_length=3, verbose_name='Code', blank=False, null=False)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name', blank=False, null=False)
    language = models.ManyToManyField(Language, verbose_name='Language', default=None)

    def __str__(self):
        return self.name


class Producer(models.Model):
    first_name = models.CharField(max_length=128, verbose_name='First Name', blank=False, null=False)
    last_name = models.CharField(max_length=128, verbose_name='Last Name', blank=False, null=False)
    middle_name = models.CharField(max_length=128, verbose_name='Middle Name', blank=False, null=False)
    country = models.ManyToManyField(Country, verbose_name='Country', default=None)
    language = models.ManyToManyField(Language, verbose_name='Language', default=None)


class Director(Producer):
    ...


class Actor(Producer):
    ...


class Genre(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name', blank=False, null=False)


class Movie(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name', blank=False, null=False)
    genre = models.ManyToManyField(Genre, verbose_name='Genre', blank=False)
    release_date = models.DateField(verbose_name='Release Date', blank=False, null=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Rating', blank=False, null=False)
    duration = models.PositiveIntegerField(
        verbose_name='Duration', help_text='Длительность фильма в секундах', blank=False, null=False
    )
    actor = models.ManyToManyField(Actor, verbose_name='Actor', default=None)
    director = models.ForeignKey(Director, verbose_name='Director', blank=False, null=False, on_delete=models.CASCADE)

    country = models.ManyToManyField(Country, verbose_name='Country', default=None)
    language = models.ManyToManyField(Language, verbose_name='Language', default=None)


class FavoriteMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING, verbose_name='Favorite Movie')
    user = models.ForeignKey(USER, on_delete=models.DO_NOTHING, verbose_name='User')
