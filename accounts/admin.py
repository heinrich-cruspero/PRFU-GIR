from datetime import date

from django import forms
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext as _

from .models import UserProfile, Contact, Waiver
from affiliations.models import Affiliation
from events.models import Event


from inline_actions.admin import InlineActionsMixin
from inline_actions.admin import InlineActionsModelAdminMixin
from inline_actions.actions import DefaultActionsMixin, ViewAction


class CustomUserCreationForm(UserCreationForm):
    """
    A UserCreationForm with optional password inputs.
    """
    middle_name = forms.CharField(label='Phone Number', required=False)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = super(CustomUserCreationForm, self).clean_password2()
        if bool(password1) ^ bool(password2):
            raise forms.ValidationError("Fill out both fields")
        return password2


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

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


class ChangeWaiverMixin(object):

    def get_inline_actions(self, request, obj=None):
        actions = super(ChangeWaiverMixin,
                        self).get_inline_actions(request, obj)

        if obj:
            try:
                waiver = Waiver.objects.get(
                    userprofile__id=obj.userprofile_id,
                    event__id=obj.event.id,
                )
                actions.append('remove_waiver')
            except Waiver.DoesNotExist:
                actions.append('add_wavier')

        return actions

    def add_wavier(self, request, obj, parent_obj=None):
        userprofile = UserProfile.objects.get(id=obj.userprofile_id)
        event = Event.objects.get(id=obj.event.id)

        Waiver.objects.create(
            userprofile=userprofile,
            event=event,
        )
        message = "Added waiver to event: {}".format(obj.event)
        messages.success(request, _(message))
    add_wavier.short_description = _("Add Waiver")

    def remove_waiver(self, request, obj, parent_obj=None):
        waiver = Waiver.objects.get(
            userprofile__id=obj.userprofile_id,
            event__id=obj.event.id,
        )

        waiver.delete()

        message = "Removed waiver to event: {}".format(obj.event)
        messages.error(request, _(message))
    remove_waiver.short_description = _("Remove Waiver")


class EventInline(ChangeWaiverMixin,
                  InlineActionsMixin,
                  admin.TabularInline):

    model = Event.participants.through
    verbose_name = "Event"
    verbose_name_plural = "My Events"

    # def has_add_permission(self, request):
    #     return False


class AffiliationInline(admin.TabularInline):
    model = Affiliation.members.through
    verbose_name = "Affiliation"
    verbose_name_plural = "My Affiliations"


class UserProfileAdmin(InlineActionsModelAdminMixin,
                       admin.ModelAdmin):

    model = UserProfile

    inlines = [
        AffiliationInline,
        EventInline,
    ]

    exclude = (
        'events',
        'age',
    )
    list_filter = (AgeGroupListFilter,)

    list_display = (
        'id',
        'last_name',
        'first_name',
        'middle_name',
        'age'
    )

    search_fields = (
        'first_name',
        'last_name',
    )

    PERSONAL_INFO = [
        'last_name',
        'first_name',
        'middle_name',
        'date_of_birth',
        'gender',
    ]

    CONTACT_INFO = [
        'mobile',
        'email',
        'address',
        'city',
        # 'country',
        # 'level',
        # 'course',
        # 'emergency_contact',
    ]

    ACADEMIC_INFO = [
        'level',
        'course',
    ]

    VITALS_INFO = [
        'weight',
        'height',
        'wingspan',
        'blood_type',
    ]

    fieldsets = [
        ('PERSONAL INFORMATION', {'fields': PERSONAL_INFO}),
        ('CONTACT INFORMATION', {'fields': CONTACT_INFO}),
        ('ACADEMIC INFORMATION', {'fields': ACADEMIC_INFO}),
        # ('VITALS', {'fields': VITALS_INFO}),
    ]

class WaiverAdmin(admin.ModelAdmin):
    model = Waiver

    list_display = (
        'event',
        'userprofile',
    )

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Contact)
admin.site.register(Waiver, WaiverAdmin)
