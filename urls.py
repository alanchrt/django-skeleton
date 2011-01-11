from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {
        'template': 'home.html',
    }, 'home'),

    (r'^admin_tools/', include('admin_tools.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
                'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

    )
