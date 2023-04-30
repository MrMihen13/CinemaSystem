from django.contrib import admin

from ticket import models


@admin.register(models.PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ('hall', 'price', 'places')


@admin.register(models.Ticket)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ('session', 'price', 'user')
