#!/usr/bin/env python
import os
import sys
import random
import shutil
import string
from django.core.management import execute_manager

project = lambda path: os.path.join(os.path.dirname(__file__), path)

if __name__ == "__main__":
    if sys.argv[1] == 'configure':
        # Attempt to import configuration or create file
        try:
            from settings.environment import *
        except RuntimeError:
            shutil.copyfile(project('settings/environment.example.py'),
                            project('settings/environment.py'))

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
                                'django.db.backends.[[DB_ENGINE]]'):
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
            DATABASES['default']['NAME'] = raw_input("Database name [" +
                                         project('database.sqlite') + "]: ")
            if DATABASES['default']['NAME'] == '':
                DATABASES['default']['NAME'] = project('database.sqlite')
            new_data = new_data.replace('[[DB_NAME]]',
                                                DATABASES['default']['NAME'])

        # Write the revised configuration
        if new_data != original_data:
            o = open(project('settings/environment.py'), 'w')
            o.write(new_data)
            o.close()

        import sys
        sys.exit()
    else:
        try:
            import settings # Assumed to be in the same directory.
        except ImportError:
            import sys
            sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
            sys.exit(1)
        execute_manager(settings)
