from django.contrib import admin

from cinema import models


@admin.register(models.Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone')


@admin.register(models.Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('number', 'cinema', 'rows_count', 'seats_count')
    list_filter = ('cinema', 'rows_count', 'seats_count')
