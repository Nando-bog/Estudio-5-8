# coding=utf-8

import os
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = 't-5s+-dalv%cd1nk_!-l*y8i2nr7nwdm#!b#q3=9p23snk_!qr'

# if DATABASES:
#     pass
# else:
#     DATABASES = {
#         'default': {
#             dj_database_url.config()
#         #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         #     'NAME': 'estudio5_8',
#         #     'USER': 'admin5_8',
#         #     'PASSWORD': 'admin',
#         #     'HOST': 'localhost',
#         #     'PORT': '5432',
#         }
#     }
#HEROKU CONFIGURATION
# Parse database configuration from $DATABASE_URL

#DATABASES['default'] = dj_database_url.config()
#DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2' 

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
