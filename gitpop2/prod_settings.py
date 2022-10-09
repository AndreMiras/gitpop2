import os

from .base_settings import *  # noqa: F401, F403

DEBUG = False

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

ADMINS = ((os.environ["ADMIN_NAME"], os.environ["ADMIN_EMAIL"]),)

MANAGERS = ADMINS
