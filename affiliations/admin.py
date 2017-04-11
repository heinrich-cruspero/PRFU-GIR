from django.contrib import admin


from .models import Affiliation


class AffiliationAdmin(admin.ModelAdmin):
    model = Affiliation

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name',
                'address',
                'classification',
                'contact',
            )}
         ),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super(AffiliationAdmin, self).get_fieldsets(request, obj)

admin.site.register(Affiliation, AffiliationAdmin)
