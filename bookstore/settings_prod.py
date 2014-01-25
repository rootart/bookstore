from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SOUTH_TESTS_MIGRATE = False
SOUTH_DATABASE_ADAPTER='south.db.psycopg2'
SKIP_SOUTH_TESTS = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'bookstore.db'),
        'USER': '', 
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
print os.path.join(PROJECT_DIR, 'bookstore.db')

if not DEBUG:
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = 'ur!i@&amp;t56z&amp;=pwwcj3^oi))b9w50a*&amp;mju#q@v%2l!l7^ze5-('
