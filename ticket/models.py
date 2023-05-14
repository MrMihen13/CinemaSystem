from django.db import models

from django.contrib.auth import get_user_model

from session import models as session_models

USER = get_user_model()


class Ticket(models.Model):
    user = models.ForeignKey(USER, verbose_name='User', on_delete=models.CASCADE)
    session = models.ForeignKey(session_models.Session, verbose_name='Session', on_delete=models.CASCADE)
    price = models.ForeignKey(session_models.PriceList, verbose_name='Price', on_delete=models.CASCADE)
