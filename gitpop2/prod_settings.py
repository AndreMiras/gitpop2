from base_settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()


