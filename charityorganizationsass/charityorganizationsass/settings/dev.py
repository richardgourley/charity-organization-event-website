from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

# CONSOLE EMAIL BACKEND - TESTING
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# FILE BASED EMAIL BACKEND - TESTING
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = str(BASE_DIR + '/sent_emails')

try:
    from .local import *
except ImportError:
    pass