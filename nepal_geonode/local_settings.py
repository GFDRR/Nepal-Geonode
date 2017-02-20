# from .settings import INSTALLED_APPS, MIDDLEWARE_CLASSES, PROJECT_ROOT
# import os

# DEFAULT_TOPICCATEGORY = 'location'

# # django debug toolbar
# DEBUG_TOOLBAR_PATCH_SETTINGS = False
# INSTALLED_APPS += ('debug_toolbar', 'geonode-client',)
# MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
# INTERNAL_IPS = ('127.0.0.1', )
# #

# SITEURL = "http://localhost:8000/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nepal_geonode',
        'USER': 'nepal_geonode',
        'PASSWORD': 'nepal_geonode',
    },

    # vector datastore for uploads
    'datastore': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'ENGINE': '',  # Empty ENGINE name disables
        'NAME': 'nepal_geonode_app',
        'USER': 'nepal_geonode',
        'PASSWORD': 'nepal_geonode',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# GEOSERVER_LOCATION = os.getenv(
#     'GEOSERVER_LOCATION', 'http://localhost:8080/geoserver/'
# )
# GEOSERVER_PUBLIC_LOCATION = os.getenv(
#     'GEOSERVER_PUBLIC_LOCATION', 'http://localhost:8080/geoserver/'
# )

# # OGC (WMS/WFS/WCS) Server Settings
# OGC_SERVER = {
#     'default': {
#         'BACKEND': 'geonode.geoserver',
#         'LOCATION': 'http://localhost:8080/geoserver/',
#         'PUBLIC_LOCATION': 'http://localhost:8080/geoserver/',
#         'USER': 'admin',
#         'PASSWORD': 'geoserver',
#         'MAPFISH_PRINT_ENABLED': True,
#         'PRINT_NG_ENABLED': True,
#         'GEONODE_SECURITY_ENABLED': True,
#         'GEOGIG_ENABLED': False,
#         'WMST_ENABLED': False,
#         'BACKEND_WRITE_ENABLED': True,
#         'WPS_ENABLED': False,
#         'LOG_FILE': '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
#         # Set to dictionary identifier of database containing spatial data in DATABASES dictionary to enable
#         'DATASTORE': '',  # 'datastore',
#     }
# }

# CATALOGUE = {
#     'default': {
#         # The underlying CSW implementation
#         # default is pycsw in local mode (tied directly to GeoNode Django DB)
#         'ENGINE': 'geonode.catalogue.backends.pycsw_local',
#         # pycsw in non-local mode
#         # 'ENGINE': 'geonode.catalogue.backends.pycsw_http',
#         # GeoNetwork opensource
#         # 'ENGINE': 'geonode.catalogue.backends.geonetwork',
#         # deegree and others
#         # 'ENGINE': 'geonode.catalogue.backends.generic',

#         # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
#         'URL': '%scatalogue/csw' % SITEURL,
#         # 'URL': 'http://localhost:8080/geonetwork/srv/en/csw',
#         # 'URL': 'http://localhost:8080/deegree-csw-demo-3.0.4/services',

#         # login credentials (for GeoNetwork)
#         'USER': 'admin',
#         'PASSWORD': 'admin',
#     }
# }
