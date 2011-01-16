DEBUG = [[DEBUG]]
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('[[YOUR_NAME]]', '[[YOUR EMAIL]]'),
)

MANAGERS = ADMINS

SECRET_KEY = '[[SECRET_KEY]]'

MEDIA_URL = '[[MEDIA_URL]]'
ADMIN_MEDIA_PREFIX = '[[ADMIN_MEDIA_PREFIX]]' 
CACHE_BACKEND = '[[CACHE_BACKEND]]'

DATABASES = {
    'default': {
        # Backends: 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.[[DB_ENGINE]]',
        'NAME': '[[DB_NAME]]',                         
        'USER': '[[DB_USER]]',                         
        'PASSWORD': '[[DB_PASSWORD]]',                 
        'HOST': '[[DB_HOST]]',                                    
        'PORT': '[[DB_PORT]]',
    }
}
