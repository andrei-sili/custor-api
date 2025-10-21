from .base import *

DEBUG = True

DATABASES["default"] = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": getenv("DB_NAME", "custor_dev"),
    "USER": getenv("DB_USER", "custor"),
    "PASSWORD": getenv("DB_PASSWORD", "custor"),
    "HOST": getenv("DB_HOST", "db"),
    "PORT": getenv("DB_PORT", "5432"),
}

ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost,dev.custor.local").split(",")

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = getenv(
    "CORS_ALLOWED_ORIGINS",
    "http://127.0.0.1:3000,http://localhost:3000"
).split(",")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
LOGGING["root"]["level"] = "DEBUG"
