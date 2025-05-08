from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

#class StaticStorage(S3Boto3Storage):
#    location = 'static'
#    default_acl = 'public-read'

#class MediaStorage(S3Boto3Storage):
#    location = 'media'
#    default_acl = 'public-read'
#    file_overwrite = False

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3Boto3Storage'