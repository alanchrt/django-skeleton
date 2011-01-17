import random
import shutil
import string
from settings import project

try:
    from settings.environment import *
except ImportError:
    shutil.copyfile(project('settings/environment.example.py'),
                    project('settings/environment.py'))

def migrate():
    """Auto-configure the project environment."""
    # Get original configuration
    i = open(project('settings/environment.py'))
    new_data = original_data = i.read()
    i.close()

    # Check debug mode configuration
    try:
        if DEBUG == None:
            raise Exception, "Not configured"
    except:
        DEBUG = raw_input("Debug mode [True]: ")
        if DEBUG == '':
            DEBUG = 'True'
        new_data = new_data.replace('DEBUG = None', 'DEBUG = ' +
                                                        DEBUG.__str__())

    # Check secret key configuration
    try:
        if SECRET_KEY == '[[SECRET_KEY]]':
            raise Exception, "Not configured"
    except:
        SECRET_KEY = ''.join(random.choice(string.letters + string.digits +
                       string.punctuation.replace('\'', ''))
                       for x in range(60))
        new_data = new_data.replace('[[SECRET_KEY]]', SECRET_KEY)

    # Check media url configuration
    try:
        if MEDIA_URL == '[[MEDIA_URL]]':
            raise Exception, "Not configured"
    except:
        MEDIA_URL = raw_input("Media URL [/media/]: ")
        if MEDIA_URL == '':
            MEDIA_URL = '/media/'
        new_data = new_data.replace('[[MEDIA_URL]]', MEDIA_URL)

    # Check admin media prefix configuration
    try:
        if ADMIN_MEDIA_PREFIX == '[[ADMIN_MEDIA_PREFIX]]':
            raise Exception, "Not configured"
    except:
        ADMIN_MEDIA_PREFIX = raw_input("Admin media prefix " +
                               "[http://localhost:8000/media/admin/]: ")
        if ADMIN_MEDIA_PREFIX == '':
            ADMIN_MEDIA_PREFIX = 'http://localhost:8000/media/admin/'
        new_data = new_data.replace('[[ADMIN_MEDIA_PREFIX]]',
                                                    ADMIN_MEDIA_PREFIX)

    # Check cache backend configuration
    try:
        if CACHE_BACKEND == '[[CACHE_BACKEND]]':
            raise Exception, "Not configured"
    except:
        CACHE_BACKEND = raw_input("Cache backend [dummy://]: ")
        if CACHE_BACKEND == '':
            CACHE_BACKEND = 'dummy://'
        new_data = new_data.replace('[[CACHE_BACKEND]]', CACHE_BACKEND)

    # Check database backend configuration
    try:
        if (DATABASES['default']['ENGINE'] ==
                            'django.db.backends.[[DB_BACKEND]]'):
            raise Exception, "Not configured"
    except:
        database_backend = raw_input("Database backend " +
             "('postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3', " +
             "or 'oracle') [sqlite3]: ")
        if database_backend == '':
            database_backend = 'sqlite3'
        try:
            DATABASES['default']['ENGINE'] = ('django.db.backends.' +
                                                        database_backend)
        except NameError:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.' + database_backend,
                }
            }
        new_data = new_data.replace('[[DB_BACKEND]]', database_backend)
     
    # Check database name configuration
    try:
        if (DATABASES['default']['NAME'] == '[[DB_NAME]]'):
            raise Exception, "Not configured"
    except:
        if DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
            default = project('database.sqlite')
        else:
            default = ''
        DATABASES['default']['NAME'] = raw_input("Database name [" +
                                     default + "]: ")
        if DATABASES['default']['NAME'] == '':
            DATABASES['default']['NAME'] = default
        new_data = new_data.replace('[[DB_NAME]]',
                                            DATABASES['default']['NAME'])

    # Check database user configuration
    try:
        if (DATABASES['default']['USER'] == '[[DB_USER]]'):
            raise Exception, "Not configured"
    except:
        if DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
            DATABASES['default']['USER'] = ''
        else:
            DATABASES['default']['USER'] = raw_input("Database user []: ")
        new_data = new_data.replace('[[DB_USER]]',
                                        DATABASES['default']['USER'])

    # Check database password configuration
    try:
        if (DATABASES['default']['PASSWORD'] == '[[DB_PASSWORD]]'):
            raise Exception, "Not configured"
    except:
        if DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
            DATABASES['default']['PASSWORD'] = ''
        else:
            DATABASES['default']['PASSWORD'] = raw_input("Database " +
                                                          "password []: ")
        new_data = new_data.replace('[[DB_PASSWORD]]',
                                        DATABASES['default']['PASSWORD'])

    # Check database host configuration
    try:
        if (DATABASES['default']['HOST'] == '[[DB_HOST]]'):
            raise Exception, "Not configured"
    except:
        if DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
            DATABASES['default']['HOST'] = ''
        else:
            DATABASES['default']['HOST'] = raw_input("Database " +
                                                      "host [localhost]: ")
        new_data = new_data.replace('[[DB_HOST]]',
                                        DATABASES['default']['HOST'])

    # Check database port configuration
    try:
        if (DATABASES['default']['PORT'] == '[[DB_PORT]]'):
            raise Exception, "Not configured"
    except:
        if DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
            DATABASES['default']['PORT'] = ''
        else:
            DATABASES['default']['PORT'] = raw_input("Database " +
                                  "port [default for database engine]: ")
        new_data = new_data.replace('[[DB_PORT]]',
                                        DATABASES['default']['PORT'])

    # Write the revised configuration
    if new_data != original_data:
        o = open(project('settings/environment.py'), 'w')
        o.write(new_data)
        o.close()
