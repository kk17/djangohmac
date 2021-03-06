"""
Dummy django settings
"""

import os

SECRET_KEY = 'hailthesunshine'

MEDIA_ROOT = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = '/media/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'djangohmac.middleware.HmacMiddleware',
)

HMAC_SECRET = 'HMAC_SECRET'
HMAC_SECRETS = {
    'serviceA': 'HMAC_SERVICE_A_SECRET',
    'serviceB': 'HMAC_SERVICE_B_SECRET'
}
# HMAC_HEADER = HMAC_HEADER
# HMAC_DIGESTMOD = HMAC_DIGESTMOD
# HMAC_DISABLE = HMAC_DISABLE
