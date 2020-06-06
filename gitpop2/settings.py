import os

if os.environ.get("PRODUCTION"):
    from .prod_settings import *  # noqa: F401, F403
else:
    from .dev_settings import *  # noqa: F401, F403
