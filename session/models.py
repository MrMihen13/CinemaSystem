from django.db import models

from cinema import models as cinema_models
from movie import models as movie_models


class Session(models.Model):
    cinema = models.ForeignKey(cinema_models.Cinema, verbose_name='Cinema', on_delete=models.CASCADE)
    hall = models.ForeignKey(cinema_models.Hall, verbose_name='Hall', on_delete=models.CASCADE)
    movie = models.ForeignKey(movie_models.Movie, verbose_name='Movie', on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name='Start time', blank=False, null=False)
