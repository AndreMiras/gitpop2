"""
WSGI config for gitpop2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gitpop2.settings")

application = get_wsgi_application()

# as expected by Vercel, refs:
# https://vercel.com/docs/runtimes#advanced-usage/advanced-python-usage
app = application
