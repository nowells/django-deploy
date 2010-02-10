import os

from __PROJECT_NAME__.settings import SITE_ROOT

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
    )

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.auth',
    )

ROOT_URLCONF = '__PROJECT_NAME__.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    )
