from django import forms
from django.contrib import admin

from .models import Event
from accounts.models import UserProfile


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end',)
    search_fields = ('name', 'start', 'end',)

    filter_horizontal = ('participants',)

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == "participants":
    #         kwargs["queryset"] = UserProfile.objects.filter(user__last_name__contains='Cruspero')
    #     return super(EventAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Event, EventAdmin)
