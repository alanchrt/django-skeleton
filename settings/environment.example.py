DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('Your Name', 'email@company.com'),
)

MANAGERS = ADMINS

SECRET_KEY = ''

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = 'http://127.0.0.1:8000/media/admin/'
CACHE_BACKEND = 'dummy://'

INTERNAL_IPS = (
    '127.0.0.1',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
