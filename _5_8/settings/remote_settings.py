# coding=utf-8

import os
import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


##### VARIABLES TOMADAS DEL OS -en versión local están "hard coded" ######
##### NO OLVIDE CAMBIAR ESTO PARA PRODUCCION ######
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')



ALLOWED_HOSTS = ['*']

##HEROKU DATABASE
# Parse database configuration from $DATABASE_URL
DATABASES = {}
DATABASES['default'] = dj_database_url.config()

# Enable Persistent Connections
DATABASES['default']['CONN_MAX_AGE'] = 500

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

##AWS CREDENTIALS DO NOT UPLOAD TO GIT DO NOT DO NOT DO NOT UPLOAD TO GIT

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

    # Tell django-storages that when coming up with the URL for an item in S3 storage, keep
    # it simple - just use this domain plus the path. (If this isn't set, things get complicated).
    # This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
    # We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

    # This is used by the `static` template tag from `static`, if you're using that. Or if anything else
    # refers directly to STATIC_URL. So it's safest to always set it.
STATIC_URL = "https://{0}/".format(AWS_S3_CUSTOM_DOMAIN)

STATIC_ROOT = "https://{0}/".format(AWS_S3_CUSTOM_DOMAIN, 'static')

    # Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
    # you run `collectstatic`).
    
MEDIA_URL = "https://{0}/".format(AWS_S3_CUSTOM_DOMAIN)
MEDIA_ROOT = "https://{0}/".format(AWS_S3_CUSTOM_DOMAIN)
    
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

##---RECAPTCHA CONFIGURATION ---##
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')