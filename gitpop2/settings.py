import os

if os.environ.get('PRODUCTION'):
    from prod_settings import *
else:
    from dev_settings import *
