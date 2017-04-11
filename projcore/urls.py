from __future__ import (
    absolute_import,
)

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from projcore.views import (
    HomeView,
)

urlpatterns = [
    # url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.MEDIA_ROOT
#         })
#     ]
