from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext as _

from .models import UserProfile

from datetime import date


class ProjectCustomUserAdmin(UserAdmin):

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2'
            )}
         ),
    )


class AgeGroupListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Age Group')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('Juniors', _('Juniors')),
            ('Seniors', _('Seniors')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'Juniors':
            return queryset.filter(age__lte=15)
        if self.value() == 'Seniors':
            return queryset.filter(age__gt=15)


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    exclude = (
        'events',
        'age',
    )
    list_filter = (AgeGroupListFilter,)

    list_display = (
        'id',
        'get_last_name',
        'get_first_name',
        'get_email',
        'get_username',
        'age'
    )

    search_fields = (
        'user__first_name',
        'user__last_name',
        'user__username'
    )

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_email(self, obj):
        return obj.user.email

    def get_username(self, obj):
        return obj.user.username

    get_last_name.short_description = 'Surname'
    get_last_name.admin_order_field = 'user__last_name'

    get_first_name.short_description = 'First Name'
    get_first_name.admin_order_field = 'user__first_name'

    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'

    get_username.short_description = 'Username'
    get_username.admin_order_field = 'user__username'


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, ProjectCustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
