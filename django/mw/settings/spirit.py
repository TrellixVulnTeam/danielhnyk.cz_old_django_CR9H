from spirit.settings import *
from .common import *

SITE_ID = 4 # spirit.danielhnyk.cz

INSTALLED_APPS += ( "djrill",)

MANDRILL_API_KEY = "j2Go0h1D1CM4kdhyYxHh7w"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
DEFAULT_FROM_EMAIL = "kotrfa@gmail.com"
