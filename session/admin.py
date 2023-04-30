from django.contrib import admin

from session import models


@admin.register(models.Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('movie', 'hall', 'cinema', 'start_time')
