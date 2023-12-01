from .base import *

import os


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

HOST_NAME = os.getenv("HOST_NAME")

ALLOWED_HOSTS = [HOST_NAME]


# Cache
REDIS_USERNAME = os.getenv("REDIS_USERNAME")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_KEY_PREFIX = os.getenv("REDIS_KEY_PREFIX")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_USERNAME}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/",
        "KEY_PREFIX": f"{REDIS_KEY_PREFIX}",
        'OPTIONS': {
            'CLIENT_CLASS': 'helpers.custom_redis_cluster.CustomRedisCluster',
        }
    }
}
