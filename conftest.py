import os
from django.conf import settings
import pytest

DEFAULT_ENGINE = 'django.db.backends.postgresql_psycopg2'

@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": os.environ.get("SQL_ENGINE", DEFAULT_ENGINE),
        "HOST": os.environ["SQL_HOST"],
        "NAME": os.environ["SQL_DATABASE"],
        "PORT": os.environ["SQL_PORT"],
        "USER": os.environ["SQL_PORT"],
        "PASSWORD": os.environ["SQL_PASSWORD"],

    }