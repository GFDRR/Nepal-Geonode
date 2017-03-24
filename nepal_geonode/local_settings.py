import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

SITEURL = "http://geonode.ashishacharya.com/"

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

GEOSERVER_LOCATION = os.getenv(
    'GEOSERVER_LOCATION', 'http://localhost:8080/geoserver/'
)
GEOSERVER_PUBLIC_LOCATION = os.getenv(
    'GEOSERVER_PUBLIC_LOCATION', 'http://geonode.ashishacharya.com/geoserver/'
)

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default': {
        'BACKEND': 'geonode.geoserver',
        'LOCATION': GEOSERVER_LOCATION,
        'LOGIN_ENDPOINT': 'j_spring_oauth2_geonode_login',
        'LOGOUT_ENDPOINT': 'j_spring_oauth2_geonode_logout',
        # PUBLIC_LOCATION needs to be kept like this because in dev mode
        # the proxy won't work and the integration tests will fail
        # the entire block has to be overridden in the local_settings
        'PUBLIC_LOCATION': GEOSERVER_PUBLIC_LOCATION,
        'USER': 'admin',
        'PASSWORD': 'geoserver',
        'MAPFISH_PRINT_ENABLED': True,
        'PRINT_NG_ENABLED': True,
        'GEONODE_SECURITY_ENABLED': True,
        'GEOGIG_ENABLED': False,
        'WMST_ENABLED': False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED': False,
        'LOG_FILE': '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
        # Set to dictionary identifier of database containing spatial data in DATABASES dictionary to enable
        'DATASTORE': 'datastore',  # 'datastore',
    }
}

# If you want to enable Mosaics use the following configuration
# UPLOADER = {
# 'BACKEND': 'geonode.rest',
#    'BACKEND': 'geonode.importer',
#    'OPTIONS': {
#        'TIME_ENABLED': True,
#        'MOSAIC_ENABLED': True,
#        'GEOGIG_ENABLED': False,
#    }
#}


CATALOGUE = {
    'default': {
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        'URL': '%scatalogue/csw' % SITEURL,
    }
}

# Default preview library
# LAYER_PREVIEW_LIBRARY = 'geoext'

MEDIA_ROOT = "/var/www/nepal_geonode/uploaded"
STATIC_ROOT = "/var/www/nepal_geonode/static"

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', ['localhost', '127.0.0.1', u'geonode.ashishacharya.com', '149.56.94.155'])
