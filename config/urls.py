from geonode.urls import *

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
