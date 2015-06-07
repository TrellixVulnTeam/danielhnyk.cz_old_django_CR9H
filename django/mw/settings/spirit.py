from spirit.settings import *
from .common import *

SITE_ID = 4 # spirit.danielhnyk.cz

WSGI_APPLICATION = 'mw.wsgi_spirit.application'
INSTALLED_APPS += ( "djrill",
                    "debug_toolbar",)

ROOT_URLCONF = 'mw.urls_spirit'
MANDRILL_API_KEY = "j2Go0h1D1CM4kdhyYxHh7w"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
DEFAULT_FROM_EMAIL = "admin@danielhnyk.cz"

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(BASE_DIR), 'others/whoosh_index'),
    },
}
