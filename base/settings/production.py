from base.settings.base import *

DEBUG = False


# Replace the DATABASES section of your settings.py with this
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PGDATABASE"),
        "USER": os.environ.get("PGUSER"),
        "PASSWORD": os.environ.get("PGPASSWORD"),
        "HOST": os.environ.get("PGHOST"),
        "PORT": os.environ.get("PGPORT", 5432),
        "OPTIONS": {
            "sslmode": "require",
        },
    }
}

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "dnb8rethz",
    "API_KEY": "123456789",
    "API_SECRET": os.environ.get("API_SECRET"),
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

STATIC_URL = os.environ.get("STATIC_URL")

BACKUP_DIRECTORY = os.path.join(BASE_DIR, "backups/production")
