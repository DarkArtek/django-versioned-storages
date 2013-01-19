from setuptools import setup, find_packages

import versioned_storages

setup(
    name = 'django-versioned-storages',
    version = versioned_storages.__version__,
    packages = find_packages(),

    author = 'Marco Paolini',
    author_email = 'marco@credra.com',
    license = 'BSD',
    description = 'Support for versioned storages',
    url='http://github.com/mpaolini/django-versioned-storages',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe = False,
)
