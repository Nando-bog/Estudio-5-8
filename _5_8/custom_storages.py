#storages.py for Proyect Estudio 5-8

##IMPORTING BOTO STORAGES BREAKS THE SYSTEM

from storages.backends.s3boto import S3BotoStorage

class StaticStorage(S3BotoStorage):
    location = 'static'

class MediaStorage(S3BotoStorage):
    location = 'uploads'

# import storages.backends.s3boto
# from dango.conf import settings
# 
# class StaticStorage(storages.backends.s3boto.S3BotoStorage):
#     location = 'static'
# 
# class MediaStorage(storages.backends.s3boto.S3BotoStorage):
#     location = 'uploads'