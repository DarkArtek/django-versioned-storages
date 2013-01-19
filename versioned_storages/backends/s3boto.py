from django.conf import settings
from storages.backends.s3boto import S3BotoStorage as OrigS3BotoStorage

STATIC_VERSION = getattr(settings, 'STATIC_VERSION', 0)
VERSIONED_LOCATION = getattr(settings, 'AWS_VERSIONED_LOCATION',
                             getattr(settings, 'AWS_LOCATION', ''))

__all__ = ['S3BotoStorage']

class S3BotoStorage(OrigS3BotoStorage):
    def __init__(self, **kwargs):
        location = '%s/%s'  % (VERSIONED_LOCATION.rstrip('/'), STATIC_VERSION)
        kwargs['location'] = location
        super(S3BotoStorage, self).__init__(**kwargs)
