DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('Your Name', 'email@company.com'),
)

MANAGERS = ADMINS

SECRET_KEY = ''

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = 'http://localhost:8000/media/admin/'
CACHE_BACKEND = 'dummy://'

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
