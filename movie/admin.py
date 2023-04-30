from django.contrib import admin

from movie import models


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.Movie)  # TODO Настроить отображение по значению жанра
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'release_date', 'duration', 'rating')


@admin.register(models.Language)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', )


@admin.register(models.Director)
class DirectorAdmin(ProducerAdmin):
    ...


@admin.register(models.Actor)
class DirectorAdmin(ProducerAdmin):
    ...


@admin.register(models.FavoriteMovie)
class FavoriteMovieAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie')
