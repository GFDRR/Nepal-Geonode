# import environ
from geonode.settings import *

SITENAME = 'nepal_geonode'

# Used for relative settings elsewhere.
ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
APPS_DIR = os.path.join(ROOT_DIR, "nepal_geonode")

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(APPS_DIR, "static"),
)

TEMPLATES[0]['DIRS'] = [os.path.join(APPS_DIR, "templates"), os.path.join(PROJECT_ROOT, "templates")]

ROOT_URLCONF = 'config.urls'

LANGUAGES = (
    ('en', 'English'),
    ('ne', 'Nepali'),
)

TIME_ZONE = "Asia/Kathmandu"

INSTALLED_APPS += ('geonode-client',)
LAYER_PREVIEW_LIBRARY = 'react'
