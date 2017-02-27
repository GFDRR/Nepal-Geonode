import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

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


SITEURL = "http://geonode.ashishacharya.com"

# OGC (WMS/WFS/WCS) Server Settings
# OGC_SERVER = {
#     'default' : {
#         'BACKEND' : 'geonode.geoserver',
#         'LOCATION' : 'http://localhost:8080/geoserver/',
#         'LOGIN_ENDPOINT': 'j_spring_oauth2_geonode_login',
#         'LOGOUT_ENDPOINT': 'j_spring_oauth2_geonode_logout',
#         'PUBLIC_LOCATION' : 'http://geonode.ashishacharya.com/geoserver/',
#         'USER' : 'admin',
#         'PASSWORD' : 'geoserver',
#         'MAPFISH_PRINT_ENABLED' : True,
#         'PRINT_NG_ENABLED' : True,
#         'GEONODE_SECURITY_ENABLED' : True,
#         'GEOGIG_ENABLED' : False,
#         'WMST_ENABLED' : False,
#         'BACKEND_WRITE_ENABLED': True,
#         'WPS_ENABLED' : False,
#         'LOG_FILE': '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
#         # Set to name of database in DATABASES dictionary to enable
#         'DATASTORE': 'nepal_geonode_app', #'datastore',
#     }
# }

# CATALOGUE = {
#     'default': {
#         'ENGINE': 'geonode.catalogue.backends.pycsw_local',
#         'URL': '%scatalogue/csw' % SITEURL,
#     }
# }

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', ['localhost', '127.0.0.1', u'geonode.ashishacharya.com'])

