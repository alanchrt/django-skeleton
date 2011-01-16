import shutil
from settings.defaults import *

try:
    from settings.environment import *
except ImportError:
    shutil.copyfile(project('settings/environment.example.py'),
                    project('settings/environment.py'))
