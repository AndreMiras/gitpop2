from base_settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

ADMINS = (
    (os.environ['ADMIN_NAME'], os.environ['ADMIN_EMAIL']),
)

MANAGERS = ADMINS

EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST= 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
