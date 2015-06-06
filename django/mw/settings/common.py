"""
Django settings for mw project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = "/var/www/danielhnyk/work_dir/django"  #os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@p6bxp=a6u-$)v@oj7krs059u27p#9h%&^bhy-s(_f6dljjaq_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['www.danielhnyk.cz', 'danielhnyk.cz']
INTERNAL_IPS = ["192.168.0.222"]


# Application definition



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ATOMIC_REQUEST': True
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Media files
MEDIA_ROOT = (os.path.join(BASE_DIR, "media"))
MEDIA_URL = '/media/'

THUMBNAIL_ALIASES = {
    '': {
        'small': {'size': (100, 100)},
        'portf': {'size': (384, 512), 'crop': True},
        'blogpost': {'size': (560, 300), 'crop': True},
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (os.path.join(BASE_DIR, "sfiles"), )
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

