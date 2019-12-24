from .common import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASE_URL = os.environ.get("DATABASE_URL")

DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL)
        }

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
