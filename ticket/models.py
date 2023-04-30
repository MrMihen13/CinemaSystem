from django.db import models

from django.contrib.auth import get_user_model

from session import models as session_models
from cinema import models as cinema_models

USER = get_user_model()


class PriceList(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price', blank=False, null=False)
    hall = models.ForeignKey(cinema_models.Hall, verbose_name='Hall', on_delete=models.CASCADE)
    places = models.PositiveIntegerField(verbose_name='Places', blank=False, null=False)  # TODO добавить проверку чтобы колличество мест не было больше чем в есть в зале

    def __str__(self):
        return self.price


class Ticket(models.Model):
    user = models.ForeignKey(USER, verbose_name='User', on_delete=models.CASCADE)
    session = models.ForeignKey(session_models.Session, verbose_name='Session', on_delete=models.CASCADE)
    price = models.ForeignKey(PriceList, verbose_name='Price', on_delete=models.CASCADE)
