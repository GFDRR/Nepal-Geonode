# import environ
from geonode.settings import *

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
APPS_DIR = os.path.join(ROOT_DIR, "nepal_geonode")

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
