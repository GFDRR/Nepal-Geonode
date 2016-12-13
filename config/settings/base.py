# import environ
from geonode.settings import *

SITENAME = 'nepal_geonode'

# Used for relative settings elsewhere.
ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
APPS_DIR = os.path.join(ROOT_DIR, "nepal_geonode")

# OSGEO_IMPORTER = 'osgeo_importer'

# IMPORT_HANDLERS = [
#     # If GeoServer handlers are enabled, you must have an instance of geoserver running.
#     # Warning: the order of the handlers here matters.
#     'osgeo_importer.handlers.FieldConverterHandler',
#     'osgeo_importer.handlers.geoserver.GeoserverPublishHandler',
#     'osgeo_importer.handlers.geoserver.GeoserverPublishCoverageHandler',
#     'osgeo_importer.handlers.geoserver.GeoServerTimeHandler',
#     'osgeo_importer.handlers.geoserver.GeoWebCacheHandler',
#     'osgeo_importer.handlers.geoserver.GeoServerBoundsHandler',
#     'osgeo_importer.handlers.geoserver.GenericSLDHandler',
#     'osgeo_importer.handlers.geonode.GeoNodePublishHandler',
#     'osgeo_importer.handlers.geoserver.GeoServerStyleHandler',
#     'osgeo_importer.handlers.geonode.GeoNodeMetadataHandler'
# ]

# OSGEO_DATASTORE = 'datastore'
# OSGEO_IMPORTER_GEONODE_ENABLED = True
# OSGEO_IMPORTER_VALID_EXTENSIONS = [
#     'shp', 'shx', 'prj', 'dbf', 'kml', 'geojson', 'json', 'tif', 'tiff',
#     'gpkg', 'csv', 'zip', 'xml', 'sld'
# ]

# MEDIA_ROOT =
# STATIC_ROOT =
# STATICFILES_DIRS =

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(PROJECT_ROOT, "templates")],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.contrib.auth.context_processors.auth',
#                 'django.core.context_processors.debug',
#                 'django.core.context_processors.i18n',
#                 'django.core.context_processors.tz',
#                 'django.core.context_processors.media',
#                 'django.core.context_processors.static',
#                 'django.core.context_processors.request',
#                 'django.contrib.messages.context_processors.messages',
#                 'account.context_processors.account',
#                 'geonode.context_processors.resource_urls',
#                 'geonode.geoserver.context_processors.geoserver_urls',
#             ],
#             'debug': DEBUG,
#         },
#     },
# ]

# OGC_SERVER = {
#     'default': {
#         'BACKEND': 'geonode.geoserver',
#         'LOCATION': GEOSERVER_LOCATION,
#         'LOGIN_ENDPOINT': 'j_spring_oauth2_geonode_login',
#         'LOGOUT_ENDPOINT': 'j_spring_oauth2_geonode_logout',
#         # PUBLIC_LOCATION needs to be kept like this because in dev mode
#         # the proxy won't work and the integration tests will fail
#         # the entire block has to be overridden in the local_settings
#         'PUBLIC_LOCATION': GEOSERVER_PUBLIC_LOCATION,
#         'USER': 'admin',
#         'PASSWORD': 'geoserver',
#         'MAPFISH_PRINT_ENABLED': True,
#         'PRINT_NG_ENABLED': True,
#         'GEONODE_SECURITY_ENABLED': True,
#         'GEOGIG_ENABLED': False,
#         'WMST_ENABLED': False,
#         'BACKEND_WRITE_ENABLED': True,
#         'WPS_ENABLED': False,
#         'LOG_FILE': '%s/geoserver/data/logs/geoserver.log'
#         % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
#         # Set to name of database in DATABASES dictionary to enable
#         'DATASTORE': '',  # 'datastore',
#         'PG_GEOGIG': False,
#         'TIMEOUT': 10  # number of seconds to allow for HTTP requests
#     }
# }

# Setting TWITTER_CARD to True will enable Twitter Cards
# https://dev.twitter.com/cards/getting-started
# Be sure to replace @GeoNode with your organization or site's twitter handle.
# TWITTER_CARD = True
# TWITTER_SITE = '@GeoNode'
# TWITTER_HASHTAGS = ['geonode']
