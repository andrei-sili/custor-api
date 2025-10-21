from .base import *

DEBUG = False

DATABASES["default"] = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": getenv("DB_NAME"),       # required in env
    "USER": getenv("DB_USER"),       # required in env
    "PASSWORD": getenv("DB_PASSWORD"),
    "HOST": getenv("DB_HOST"),
    "PORT": getenv("DB_PORT", "5432"),
}

ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS", "").split(",")

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = getenv("CORS_ALLOWED_ORIGINS", "").split(",")

# Security hardening (behind reverse proxy/ingress with TLS)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Optional: HSTS, CSP etc.
LOGGING["root"]["level"] = "INFO"
