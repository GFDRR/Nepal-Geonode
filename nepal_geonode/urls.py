from django.conf import settings
from django.conf.urls import include, url

from geonode.urls import *

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name='homepage.html'),
        name='home'),
] + urlpatterns


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
