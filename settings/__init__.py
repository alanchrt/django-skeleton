from settings.defaults import *

try:
    from settings.environment import *
except ImportError:
    raise RuntimeError("Your environment settings are not configured. " +
        "Please manually create and configure settings/environment.py.")
