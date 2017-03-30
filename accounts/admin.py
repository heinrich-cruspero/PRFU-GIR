from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


from .models import UserProfile

from datetime import date


class MyUserAdmin(UserAdmin):
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


# class AgeGroupListFilter(admin.SimpleListFilter):
#     # Human-readable title which will be displayed in the
#     # right admin sidebar just above the filter options.
#     title = _('decade born')

#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = 'decade'

#     def lookups(self, request, model_admin):
#         """
#         Returns a list of tuples. The first element in each
#         tuple is the coded value for the option that will
#         appear in the URL query. The second element is the
#         human-readable name for the option that will appear
#         in the right sidebar.
#         """
#         return (
#             ('80s', _('in the eighties')),
#             ('90s', _('in the nineties')),
#         )

#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         # Compare the requested value (either '80s' or '90s')
#         # to decide how to filter the queryset.
#         if self.value() == '80s':
#             return queryset.filter(birthday__gte=date(1980, 1, 1),
#                                     birthday__lte=date(1989, 12, 31))
#         if self.value() == '90s':
#             return queryset.filter(birthday__gte=date(1990, 1, 1),
#                                     birthday__lte=date(1999, 12, 31))



class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    exclude = ('events',)
    # list_filter = (AgeGroupListFilter,)

    list_display = (
        'id',
        'get_last_name',
        'get_first_name',
        'get_email',
        'get_username',
        'get_age'
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

    def get_queryset(self, request):
        qs = super(UserProfileAdmin, self).get_queryset(request)

        # import pdb; pdb.set_trace()
        newlist = sorted(qs, key=lambda x: x.calculate_age(), reverse=True)
        newlist = (d.id for d in newlist)

        return UserProfile.objects.filter(id__in=newlist)

    def get_age(self, obj):
        return obj.calculate_age()

    get_last_name.short_description = 'Surname'
    get_last_name.admin_order_field = 'user__last_name'

    get_first_name.short_description = 'First Name'
    get_first_name.admin_order_field = 'user__first_name'

    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'

    get_username.short_description = 'Username'
    get_username.admin_order_field = 'user__username'

    get_age.short_description = 'Age'
    # get_age.admin_order_field = 'get_age'


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
