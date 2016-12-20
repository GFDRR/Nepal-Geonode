from geonode.urls import *

urlpatterns = patterns('',
                       url(r'^/?$', TemplateView.as_view(template_name='site_index.html'), name='home'),
                       ) + urlpatterns

# django debug toolbar
if settings.DEBUG:
    try:
        import debug_toolbar
    except ImportError:
        pass
    finally:
        urlpatterns += patterns('',
                                url(r'^__debug__/', include(debug_toolbar.urls)),
                                )
