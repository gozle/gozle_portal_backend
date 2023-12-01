from __future__ import absolute_import

import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

environ = os.getenv("DJANGO_SETTINGS", "local")

if environ.endswith("local"):
    from .local import *
else:
    from .prod import *
