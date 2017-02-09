# -*- coding: utf-8 -*-

import os
import dj_database_url
import copy
from geonode.settings import *  # noqa
from geonode.settings import (
    MIDDLEWARE_CLASSES,
    STATICFILES_DIRS,
    INSTALLED_APPS,
    CELERY_IMPORTS,
    MAP_BASELAYERS,
    DATABASES,
    CATALOGUE
)


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

SITEURL = os.getenv('SITEURL', "http://geonode.ashishacharya.com/")
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
GEONODE_ROOT = os.path.abspath(os.path.dirname(geonode_path))
# Used for relative settings elsewhere.
ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
APPS_DIR = os.path.join(ROOT_DIR, "nepal_geonode")

DEBUG = str2bool(os.getenv('DEBUG', 'True'))
TEMPLATE_DEBUG = str2bool(os.getenv('TEMPLATE_DEBUG', 'False'))
DEBUG_STATIC = str2bool(os.getenv('DEBUG_STATIC', 'False'))
SECRET_KEY = os.getenv('SECRET_KEY', "02u6ws_cep$^^+vea-th+b2yuyo+$rhg)v-x&mj!p1cyt9nk+!")
# DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://nepal_geonode')
# DATABASES = {'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600), }
MANAGERS = ADMINS = os.getenv('ADMINS', [])
TIME_ZONE = "Asia/Kathmandu"
SITE_ID = int(os.getenv('SITE_ID', '1'))
USE_I18N = str2bool(os.getenv('USE_I18N', 'True'))
USE_L10N = str2bool(os.getenv('USE_I18N', 'True'))
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', "en-us")
MODELTRANSLATION_LANGUAGES = ['en', ]
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_FALLBACK_LANGUAGES = ('en',)
TEMPLATES[0]['DIRS'] = [os.path.join(APPS_DIR, "templates"), os.path.join(PROJECT_ROOT, "templates")]
MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(ROOT_DIR, "uploaded"))
MEDIA_URL = os.getenv('MEDIA_URL', "/uploaded/")
LOCAL_MEDIA_URL = os.getenv('LOCAL_MEDIA_URL', "/uploaded/")
STATIC_ROOT = os.getenv('STATIC_ROOT',
                        os.path.join(APPS_DIR, "static_root")
                        )
# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(APPS_DIR, "static"),
)
ROOT_URLCONF = os.getenv('ROOT_URLCONF', 'nepal_geonode.urls')
LOGIN_URL = os.getenv('LOGIN_URL', '/account/login/')
LOGOUT_URL = os.getenv('LOGOUT_URL', '/account/logout/')
MAX_DOCUMENT_SIZE = int(os.getenv('MAX_DOCUMENT_SIZE ', '2'))  # MB

INSTALLED_APPS = (
    'geonode',
) + INSTALLED_APPS


ALT_OSM_BASEMAPS = os.environ.get('ALT_OSM_BASEMAPS', True)
CARTODB_BASEMAPS = os.environ.get('CARTODB_BASEMAPS', True)
STAMEN_BASEMAPS = os.environ.get('STAMEN_BASEMAPS', True)
THUNDERFOREST_BASEMAPS = os.environ.get('THUNDERFOREST_BASEMAPS', True)
MAPBOX_ACCESS_TOKEN = os.environ.get('MAPBOX_ACCESS_TOKEN', None)
BING_API_KEY = os.environ.get('BING_API_KEY', None)

_INIT_DEFAULT_LAYER_SOURCE = {
    "ptype": "gxp_wmscsource",
    "url": "/geoserver/wms",
    "restUrl": "/gs/rest"
}

DEFAULT_LAYER_SOURCE = os.getenv('DEFAULT_LAYER_SOURCE', _INIT_DEFAULT_LAYER_SOURCE)

MAP_BASELAYERS = [{
    "source": {"ptype": "gxp_osmsource"},
    "type": "OpenLayers.Layer.OSM",
    "name": "OpenStreetMap",
    "visibility": True,
    "fixed": True,
    "group": "background"
}]
#MAP_BASELAYERS[0]['source']['url'] = OGC_SERVER['default']['LOCATION'] + 'wms'

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

# Add additional paths (as regular expressions) that don't require
# authentication.
AUTH_EXEMPT_URLS = ('/api/o/*', '/api/roles', '/api/adminRole', '/api/users',)

# A tuple of hosts the proxy can send requests to.
PROXY_ALLOWED_HOSTS = ()

# The proxy to use when making cross origin requests.
PROXY_URL = '/proxy/?url=' if DEBUG else None

LAYER_PREVIEW_LIBRARY = 'react'

# Require users to authenticate before using Geonode
LOCKDOWN_GEONODE = str2bool(os.getenv('LOCKDOWN_GEONODE', 'True'))

# Require users to authenticate before using Geonode
if LOCKDOWN_GEONODE:
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + \
        ('geonode.security.middleware.LoginRequiredMiddleware',)


ALLOWED_HOSTS = ['localhost', 'geonode.ashishacharya.com']

SITENAME = 'nepal_geonode'

LANGUAGES = (
    ('en', 'English'),
    ('ne', 'Nepali'),
)

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

AUTH_IP_WHITELIST = []

# Keywords thesauri
# e.g. THESAURI = [{'name':'inspire_themes', 'required':True, 'filter':True}, {'name':'inspire_concepts', 'filter':True}, ]
# Required: (boolean, optional, default false) mandatory while editing metadata (not implemented yet)
# Filter: (boolean, optional, default false) a filter option on that thesaurus will appear in the main search page
# THESAURI = []


# what does this do?
# DEFAULT_SEARCH_SIZE = '50'

# Number of results per page listed in the GeoNode search pages
CLIENT_RESULTS_LIMIT = int(os.getenv('CLIENT_RESULTS_LIMIT', '100'))

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

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
