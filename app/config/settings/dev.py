import sentry_sdk
from sentry_sdk import Hub
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

SECRETS = SECRETS_FULL['dev']

DEBUG = True
WSGI_APPLICATION = 'config.wsgi.dev.application'

sentry_sdk.init(
    dsn=SECRETS['SENTRY_DSN'],
    integrations=[DjangoIntegration()],
    send_default_pii=True,
    max_breadcrumbs=50,
    debug=True,
)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

print("os.path.join(BASE_DIR, 'db.sqlite3') >> ", os.path.join(BASE_DIR, 'db.sqlite3'))

ALLOWED_HOSTS += []
INSTALLED_APPS += []
