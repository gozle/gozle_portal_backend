from __future__ import absolute_import

import os

environ = os.getenv("DJANGO_SETTINGS", "local")

if environ.endswith("local"):
    from .local import *
else:
    from .prod import *
