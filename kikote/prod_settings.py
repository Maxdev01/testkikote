import dj_database_url

from .settings import *

DATABASES['default'] = dj_database_url.config()
DEBUG = False

SECRET_KEY = 'jw8z072=h=&e=tlr4@5ddh^x4l4i$u54ezs(!#=9u0(e+$ma%j'

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*'] 