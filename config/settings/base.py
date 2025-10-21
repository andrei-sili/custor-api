import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load .env files (common .env, then optional .env.local overrides)
try:
    from dotenv import load_dotenv

    load_dotenv(BASE_DIR / ".env", override=False)
    load_dotenv(BASE_DIR / ".env.local", override=True)
except Exception:
    # dotenv is optional in prod (you may use real env vars)
    pass


def getenv(name: str, default=None, cast=str):
    """Small helper to cast env vars."""
    val = os.getenv(name, default)
    if val is None:
        return None
    if cast is bool:
        return str(val).lower() in ("1", "true", "yes", "on")
    if cast is int:
        return int(val)
    return val


# ───────── Core Django ─────────
SECRET_KEY = getenv("DJANGO_SECRET_KEY", "insecure-local-key")
DEBUG = getenv("DJANGO_DEBUG", False, cast=bool)  # override per-env
ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Internal apps
    "apps.core",
    "apps.user",

    # Third-party
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # CORS first
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


LANGUAGE_CODE = getenv("DJANGO_LANG", "en-us")
TIME_ZONE = getenv("DJANGO_TZ", "UTC")
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ───────── Static/Media ─────────
STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_DIR / "staticfiles")
MEDIA_URL = "/media/"
MEDIA_ROOT = str(BASE_DIR / "media")

# ───────── Database (default; override per-env) ─────────
DATABASES = {
    "default": {
        "ENGINE": getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": getenv("DB_NAME", str(BASE_DIR / "db.sqlite3")),
        "USER": getenv("DB_USER", ""),
        "PASSWORD": getenv("DB_PASSWORD", ""),
        "HOST": getenv("DB_HOST", ""),
        "PORT": getenv("DB_PORT", ""),
    }
}

# ───────── Auth / DRF / JWT ─────────
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=int(getenv("JWT_ACCESS_MIN", 30))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(getenv("JWT_REFRESH_DAYS", 7))),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
}

# ───────── CORS / CSRF baseline ─────────
CORS_ALLOW_ALL_ORIGINS = getenv("CORS_ALLOW_ALL", False, cast=bool)
CORS_ALLOWED_ORIGINS = getenv("CORS_ALLOWED_ORIGINS", "").split(",") if getenv("CORS_ALLOWED_ORIGINS") else []
CSRF_TRUSTED_ORIGINS = getenv("CSRF_TRUSTED_ORIGINS", "http://127.0.0.1,http://localhost").split(",")

# ───────── Email (override per-env) ─────────
EMAIL_BACKEND = getenv("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = getenv("EMAIL_HOST", "")
EMAIL_PORT = getenv("EMAIL_PORT", "")
EMAIL_HOST_USER = getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = getenv("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = getenv("EMAIL_USE_TLS", False, cast=bool)

# ───────── Logging baseline ─────────
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "[{levelname}] {name}: {message}", "style": "{"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}
