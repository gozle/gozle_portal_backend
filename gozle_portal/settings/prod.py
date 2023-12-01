from .base import *

import os


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

HOST_NAME = os.getenv("HOST_NAME")

ALLOWED_HOSTS = [HOST_NAME]
