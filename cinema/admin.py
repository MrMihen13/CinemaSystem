from django.contrib import admin

from cinema import models


@admin.register(models.Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone')


@admin.register(models.Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('number', 'cinema', 'places')
    list_filter = ('cinema', 'places')
