from django.db import models

from cinema import models as cinema_models
from movie import models as movie_models


class PriceList(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price', blank=False, null=False)
    hall = models.ForeignKey(cinema_models.Hall, verbose_name='Hall', on_delete=models.CASCADE)
    places = models.PositiveIntegerField(verbose_name='Places', blank=False, null=False)  # TODO добавить проверку чтобы колличество мест не было больше чем в есть в зале

    def __str__(self):
        return f'{self.hall.cinema} {self.hall.number} {self.price}'


class Session(models.Model):
    cinema = models.ForeignKey(cinema_models.Cinema, verbose_name='Cinema', on_delete=models.CASCADE)
    hall = models.ForeignKey(cinema_models.Hall, verbose_name='Hall', on_delete=models.CASCADE)
    movie = models.ForeignKey(movie_models.Movie, verbose_name='Movie', on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name='Start time', blank=False, null=False)
    price = models.ManyToManyField(PriceList, verbose_name='Price')
