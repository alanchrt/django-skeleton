DEBUG = None
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('Your Name', 'email@company.com'),
)

MANAGERS = ADMINS

SECRET_KEY = '[[SECRET_KEY]]'

MEDIA_URL = '[[MEDIA_URL]]'
ADMIN_MEDIA_PREFIX = '[[ADMIN_MEDIA_PREFIX]]' 
CACHE_BACKEND = '[[CACHE_BACKEND]]'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.[[DB_BACKEND]]',
        'NAME': '[[DB_NAME]]',                         
        'USER': '[[DB_USER]]',                         
        'PASSWORD': '[[DB_PASSWORD]]',                 
        'HOST': '[[DB_HOST]]',                                    
        'PORT': '[[DB_PORT]]',
    }
}
