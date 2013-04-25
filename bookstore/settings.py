import os, sys

PROJECT_DIR = os.path.dirname(__file__)

sys.path.append(os.path.join(PROJECT_DIR, 'apps'),)
PUBLIC_DIR = os.path.join(PROJECT_DIR, 'public')

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_DIR, 'whoosh_index'),
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Etc/UTC'

LANGUAGE_CODE = 'ru'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static')

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'

)

ROOT_URLCONF = 'bookstore.urls'

WSGI_APPLICATION = 'bookstore.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'catalogue.context_processors.defaults'
)

ABOUT_US_DEFAULT_IMAGE = os.path.join(MEDIA_ROOT, 'about_us.JPG')

FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, 'fixtures'),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, '..', 'locale'),
)

PROJECT_APPS = (
    'catalogue',
    'subscription',
    'orders',
    'news'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django_extensions',
    'south',
    'sorl.thumbnail',
    'storages',
    'haystack',
    'pagination'
)+PROJECT_APPS

SOUTH_MIGRATION_MODULES = {
    'catalogue': 'migrations.catalogue',
    'subscription': 'migrations.subscription',
    'orders': 'migrations.orders',
    'news': 'migrations.news'
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'photo-art-ua'
AWS_ACCESS_KEY_ID = 'AKIAJXFJFZGUIHWCFXUA'
AWS_SECRET_ACCESS_KEY = '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'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

ORDER_MANAGERS = ['photoartbook.ua@gmail.com',]
DEFAULT_FROM = 'photoartbook.ua@gmail.com'
