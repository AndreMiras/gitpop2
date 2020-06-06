import os

# Parse database configuration from $DATABASE_URL
import dj_database_url

from .base_settings import *  # noqa: F403 unable to detect undefined names

DEBUG = False

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

DATABASES[  # noqa: F405 'DATABASES' may be undefined
    "default"
] = dj_database_url.config()

ADMINS = ((os.environ["ADMIN_NAME"], os.environ["ADMIN_EMAIL"]),)

MANAGERS = ADMINS

EMAIL_HOST_USER = os.environ["SENDGRID_USERNAME"]
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ["SENDGRID_PASSWORD"]
