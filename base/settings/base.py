from pathlib import Path
import os
from django.contrib.messages import constants as messages
from django.utils.translation import gettext_lazy as _


"""
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

"""


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

APP_NAME = _("Redo Developers Inc.")

SECRET_KEY = os.environ.get("SECRET_KEY")


AUTH_USER_MODEL = "accounts.Account"


# Application definition

INSTALLED_APPS = [
    "livesync",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "main",
    "debug_toolbar",
    "django_htmx",
    "accounts",
    "cloudinary_storage",
    "cloudinary",
    "maintenance_mode",
    "django_minify_html",
    "compressor",
    "django_distill",
]

MIDDLEWARE = [
    "livesync.core.middleware.DjangoLiveSyncMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
    "django_minify_html.middleware.MinifyHtmlMiddleware",
    "main.middleware.BlockIPMiddleware",
]

DJANGO_LIVESYNC = {"PORT": 8000}


ROOT_URLCONF = "base.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "main.context_processors.app",
                "django.template.context_processors.i18n",
            ],
        },
    },
]

WSGI_APPLICATION = "base.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en"

LANGUAGES = [
    ("en", _("English")),
    ("sw", _("Swahili")),
    ("fr", _("French")),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "main/locale"),
    os.path.join(BASE_DIR, "accounts/locale"),
    os.path.join(BASE_DIR, "templates/locale"),
]


TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("SMTP_EMAIL")
EMAIL_HOST_PASSWORD = os.environ.get("SMTP_PASSWORD")
EMAIL_USE_TLS = True

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

MAINTENANCE_MODE = os.environ.get("MAINTENANCE_MODE", "False").lower() == "true"
MAINTENANCE_MODE_TEMPLATE = "base/maintenance.html"
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = False
COMPRESS_ENABLED = True
COMPRESS_ROOT = os.path.join(BASE_DIR, "static")


DISTILL_SKIP_STATICFILES_DIRS = [
    ".git",
    "admin",
    "cloudinary",
    "debug_toolbar",
]
DISTILL_DIR = "D:/REDODEVS/PUBLIC/files"
