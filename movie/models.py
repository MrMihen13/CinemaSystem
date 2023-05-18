from django.db import models
from django.contrib.auth import get_user_model


USER = get_user_model()


def poster_upload_to(instance, filename: str) -> str:
    return f'movie_{instance.id}/{filename}'


def person_upload_to(instance, filename: str) -> str:
    return f'person_{instance.id}/{filename}'


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


class Person(models.Model):
    photo = models.ImageField(upload_to=person_upload_to, verbose_name='Photo', blank=True, null=True)
    first_name = models.CharField(max_length=128, verbose_name='First Name', blank=False, null=False)
    last_name = models.CharField(max_length=128, verbose_name='Last Name', blank=False, null=False)
    middle_name = models.CharField(max_length=128, verbose_name='Middle Name', blank=True, null=True)
    country = models.ManyToManyField(Country, verbose_name='Country', default=None)
    language = models.ManyToManyField(Language, verbose_name='Language', default=None)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Producer(Person):
    ...


class Director(Person):
    ...


class Actor(Person):
    ...


class Genre(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name', blank=False, null=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name', blank=False, null=False)
    genre = models.ManyToManyField(Genre, verbose_name='Genre', blank=False)
    poster = models.ImageField(upload_to=poster_upload_to, verbose_name='Poster', blank=True, null=True)
    release_date = models.DateField(verbose_name='Release Date', blank=False, null=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Rating', blank=False, null=False)
    duration = models.PositiveIntegerField(
        verbose_name='Duration', help_text='Длительность фильма в секундах', blank=False, null=False
    )
    actor = models.ManyToManyField(Actor, verbose_name='Actor', default=None)
    director = models.ForeignKey(Director, verbose_name='Director', blank=False, null=False, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, verbose_name='Producer', blank=False, null=False, on_delete=models.CASCADE)

    country = models.ManyToManyField(Country, verbose_name='Country', default=None)
    language = models.ManyToManyField(Language, verbose_name='Language', default=None)

    def __str__(self):
        return self.name


class FavoriteMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING, verbose_name='Favorite Movie')
    user = models.ForeignKey(USER, on_delete=models.DO_NOTHING, verbose_name='User')
