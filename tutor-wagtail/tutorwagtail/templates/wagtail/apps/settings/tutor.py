from .common import *
from .settings import *

SECRET_KEY = "{{ WAGTAIL_SECRET_KEY }}"
ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "mysql",
        "PORT": 3306,
        "NAME": "wagtail",
        "USER": "wagtail",
        "PASSWORD": "wagtail",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}