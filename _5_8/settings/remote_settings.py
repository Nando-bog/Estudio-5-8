# coding=utf-8

import os
import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = 't-5s+-dalv%cd1nk_!-l*y8i2nr7nwdm#!b#q3=9p23snk_!qr'

##HEROKU DATABASE
# Parse database configuration from $DATABASE_URL
DATABASES = {}
DATABASES['default'] = dj_database_url.config()

# Enable Persistent Connections
DATABASES['default']['CONN_MAX_AGE'] = 500

### HEROKU ###
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, '../staticfiles')
STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
