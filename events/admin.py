from django import forms
from django.contrib import admin

from .models import Event
from accounts.models import UserProfile


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)
    filter_horizontal = ('participants',)

    search_fields = ('name', 'date',)


admin.site.register(Event, EventAdmin)
