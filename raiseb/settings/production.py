from .base import *
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DEBUG = False


ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'codelearn.6teen@gmail.com'
#EMAIL_HOST_PASSWORD = 'nufwghjhghnxukdiykdn'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#EMAIL_USE_SSL = False
