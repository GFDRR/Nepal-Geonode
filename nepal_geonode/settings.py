# import environ
from geonode.settings import *


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


SITENAME = 'nepal_geonode'

# Used for relative settings elsewhere.
ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
APPS_DIR = os.path.join(ROOT_DIR, "nepal_geonode")

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(APPS_DIR, "static"),
)

TEMPLATES[0]['DIRS'] = [os.path.join(APPS_DIR, "templates"), os.path.join(PROJECT_ROOT, "templates")]

ROOT_URLCONF = os.getenv('ROOT_URLCONF', 'nepal_geonode.urls')

LANGUAGES = (
    ('en', 'English'),
    ('ne', 'Nepali'),
)

TIME_ZONE = "Asia/Kathmandu"

# pycsw settings
PYCSW = {
    # pycsw configuration
    'CONFIGURATION': {
        # uncomment / adjust to override server config system defaults
        # 'server': {
        #    'maxrecords': '10',
        #    'pretty_print': 'true',
        #    'federatedcatalogues': 'http://catalog.data.gov/csw'
        # },
        'metadata:main': {
            'identification_title': 'nepal_geonode Catalogue',
            'identification_abstract': 'GeoNode is an open source platform that facilitates the creation, sharing, ' \
            'and collaborative use of geospatial data',
            'identification_keywords': 'sdi,catalogue,discovery,metadata,GeoNode, nepal_geonode',
            'identification_keywords_type': 'theme',
            'identification_fees': 'None',
            'identification_accessconstraints': 'None',
            'provider_name': 'Organization Name',
            'provider_url': SITEURL,
            'contact_name': 'Acharya, Ashish',
            'contact_position': 'Developer',
            'contact_address': 'ashish.acharya14@gmail.com',
            'contact_city': 'Kathmandu',
            'contact_stateorprovince': 'Administrative Area',
            'contact_postalcode': 'Zip or Postal Code',
            'contact_country': 'Country',
            'contact_phone': '+xx-xxx-xxx-xxxx',
            'contact_fax': '+xx-xxx-xxx-xxxx',
            'contact_email': 'Email Address',
            'contact_url': 'Contact URL',
            'contact_hours': 'Hours of Service',
            'contact_instructions': 'During hours of service. Off on weekends.',
            'contact_role': 'pointOfContact',
        },
        'metadata:inspire': {
            'enabled': 'true',
            'languages_supported': 'eng,gre',
            'default_language': 'eng',
            'date': 'YYYY-MM-DD',
            'gemet_keywords': 'Utility and governmental services',
            'conformity_service': 'notEvaluated',
            'contact_name': 'Organization Name',
            'contact_email': 'Email Address',
            'temp_extent': 'YYYY-MM-DD/YYYY-MM-DD',
        }
    }
}

# define the urls after the settings are overridden
if 'geonode.geoserver' in INSTALLED_APPS:
    LOCAL_GEOSERVER = {
        "source": {
            "ptype": "gxp_wmscsource",
            "url": OGC_SERVER['default']['PUBLIC_LOCATION'] + "wms",
            "restUrl": "/gs/rest"
        }
    }
    baselayers = MAP_BASELAYERS
    MAP_BASELAYERS = [LOCAL_GEOSERVER]
    MAP_BASELAYERS.extend(baselayers)

    def get_user_url(u):
        from django.contrib.sites.models import Site
        s = Site.objects.get_current()
        return "http://" + s.domain + "/profiles/" + u.username

    _DEFAULT_ABSOLUTE_URL_OVERRIDES = {
        'auth.user': get_user_url
    }
    ABSOLUTE_URL_OVERRIDES = os.getenv('ABSOLUTE_URL_OVERRIDES', _DEFAULT_ABSOLUTE_URL_OVERRIDES)
    AUTH_PROFILE_MODULE = os.getenv('AUTH_PROFILE_MODULE', 'maps.Contact')
    REGISTRATION_OPEN = str2bool(os.getenv('REGISTRATION_OPEN', 'True'))

    ACCOUNT_ACTIVATION_DAYS = int(os.getenv('ACCOUNT_ACTIVATION_DAYS', '7'))

    # TODO: Allow overriding with an env var
    DB_DATASTORE = str2bool(os.getenv('DB_DATASTORE', 'True'))

    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', ['localhost', ])

AUTH_IP_WHITELIST = []

# Keywords thesauri
# e.g. THESAURI = [{'name':'inspire_themes', 'required':True, 'filter':True}, {'name':'inspire_concepts', 'filter':True}, ]
# Required: (boolean, optional, default false) mandatory while editing metadata (not implemented yet)
# Filter: (boolean, optional, default false) a filter option on that thesaurus will appear in the main search page
THESAURI = []


# Email for users to contact admins.
THEME_ACCOUNT_CONTACT_EMAIL = os.getenv('THEME_ACCOUNT_CONTACT_EMAIL', 'admin@example.com')


# The FULLY QUALIFIED url to the GeoServer instance for this GeoNode.
GEOSERVER_BASE_URL = os.getenv('GEOSERVER_BASE_URL',
                               "http://localhost:8001/geoserver-geonode-dev/")

# The username and password for a user that can add and edit layer details on GeoServer

_DEFAULT_GEOSERVER_CREDENTIALS = "geoserver_admin", SECRET_KEY
GEOSERVER_CREDENTIALS = os.getenv('GEOSERVER_CREDENTIALS', ("geoserver_admin", SECRET_KEY))


_INIT_DEFAULT_LAYER_SOURCE = {
    "ptype": "gxp_wmscsource",
    "url": "/geoserver/wms",
    "restUrl": "/gs/rest"
}

DEFAULT_LAYER_SOURCE = os.getenv('DEFAULT_LAYER_SOURCE', _INIT_DEFAULT_LAYER_SOURCE)

_DEFAULT_MAP_BASELAYERS = [{
    "source": {"ptype": "gxp_osmsource"},
    "type": "OpenLayers.Layer.OSM",
    "name": "mapnik",
    "visibility": True,
    "fixed": True,
    "group": "background"
}]

MAP_BASELAYERS = os.getenv('MAP_BASELAYERS', _DEFAULT_MAP_BASELAYERS)

# Setting TWITTER_CARD to True will enable Twitter Cards
# https://dev.twitter.com/cards/getting-started
# Be sure to replace @GeoNode with your organization or site's twitter handle.
# TWITTER_CARD = True
# TWITTER_SITE = '@GeoNode'
# TWITTER_HASHTAGS = ['geonode']

# Add additional paths (as regular expressions) that don't require
# authentication.
AUTH_EXEMPT_URLS = ('/api/o/*', '/api/roles', '/api/adminRole', '/api/users',)

# what does this do?
# DEFAULT_SEARCH_SIZE = '50'

# Number of results per page listed in the GeoNode search pages
CLIENT_RESULTS_LIMIT = int(os.getenv('CLIENT_RESULTS_LIMIT', '100'))

if 'geonode.geoserver' in INSTALLED_APPS:
    def get_user_url(u):
        from django.contrib.sites.models import Site
        s = Site.objects.get_current()
        return "http://" + s.domain + "/profiles/" + u.username

    _DEFAULT_ABSOLUTE_URL_OVERRIDES = {
        'auth.user': get_user_url
    }
    ABSOLUTE_URL_OVERRIDES = os.getenv('ABSOLUTE_URL_OVERRIDES', _DEFAULT_ABSOLUTE_URL_OVERRIDES)
    AUTH_PROFILE_MODULE = os.getenv('AUTH_PROFILE_MODULE', 'maps.Contact')
    REGISTRATION_OPEN = str2bool(os.getenv('REGISTRATION_OPEN', 'True'))

    ACCOUNT_ACTIVATION_DAYS = int(os.getenv('ACCOUNT_ACTIVATION_DAYS', '7'))

    # TODO: Allow overriding with an env var
    DB_DATASTORE = str2bool(os.getenv('DB_DATASTORE', 'True'))

    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', ['localhost', ])

# Keywords thesauri
# e.g. THESAURI = [{'name':'inspire_themes', 'required':True, 'filter':True}, {'name':'inspire_concepts', 'filter':True}, ]
# Required: (boolean, optional, default false) mandatory while editing metadata (not implemented yet)
# Filter: (boolean, optional, default false) a filter option on that thesaurus will appear in the main search page
THESAURI = []

# maps
LAYER_PREVIEW_LIBRARY = 'react'

# Where should newly created maps be focused?
# todo: set this to Nepal
# DEFAULT_MAP_CENTER = (0, 0)

# How tightly zoomed should newly created maps be?
# 0 = entire world;
# maximum zoom is between 12 and 15 (for Google Maps, coverage varies by area)
# DEFAULT_MAP_ZOOM = int(os.getenv('DEFAULT_MAP_ZOOM','0'))

# locale
# Location of translation files
_DEFAULT_LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, "locale"),
    os.path.join(APPS_DIR, "locale"),
)
LOCALE_PATHS = os.getenv('LOCALE_PATHS', _DEFAULT_LOCALE_PATHS)
