django-storages-versioned
==========================
a little extension to django-storages
--------------------------------------

Versioned django static storage

in your `settings.py`:

    STATIC_VERSION = 1 # defaults to 0
    AWS_VERSIONED_LOCATION = 'static' # key prefix, defaults to AWS_LOCATION
    STATICFILES_STORAGE = 'versioned_storages.storages.backends.s3boto.S3BotoStorage'
    STATIC_URL = 'http://your-aws-url.com/%s/%s/' % (AWS_STORAGE_BUCKET_NAME,
                                                  AWS_VERSIONED_LOCATION,
                                                  STATIC_VERSION)

and it will happily store your static assets in `/<aws bucket>/<STATIC_VERSION>`

WARNINIG: remember to clean up old versions of static assets
