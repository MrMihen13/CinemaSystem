from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name', blank=False, null=False)
    address = models.TextField(verbose_name='Address', blank=False, null=False)
    telephone = models.CharField(max_length=128, verbose_name='Telephone number', blank=True, null=True)
    email = models.EmailField(verbose_name='Email', blank=False, null=False)

    def __str__(self):
        return self.name


class Hall(models.Model):
    number = models.PositiveIntegerField(verbose_name='Hall number')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    places = models.PositiveIntegerField(verbose_name='Places count')

    def __str__(self):
        return f'{self.cinema} {self.number}'
