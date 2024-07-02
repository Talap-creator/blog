import os
from pathlib import Path
import dj_database_url
from decouple import config
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = [
    'web-production-62359.up.railway.app',
    'king-prawn-app-llcn9.ondigitalocean.app',
    '127.0.0.1'
]
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'blogapp',
    'django_ckeditor_5',
]

CSRF_TRUSTED_ORIGINS = [
    'https://web-production-62359.up.railway.app',
    'http://127.0.0.1'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


ROOT_URLCONF = 'blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogproject.wsgi.application'

if config('DATABASE_URL', default=None):
    DATABASES = {
        'default': dj_database_url.parse(config('DATABASE_URL'))
    }
else:
    print(".env файл не найден. Будет использовано значение по умолчанию для DATABASE_URL.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CKEDITOR_5_UPLOAD_PATH = 'uploads/'
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            {'name': 'styles', 'items': ['Format', 'Font', 'FontSize']},
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Alignment', 'Indent', 'Outdent']},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalLine', 'SpecialChar']},
            {'name': 'tools', 'items': ['Undo', 'Redo']},
        ],
        'language': 'en',
        'licenseKey': '',
        'placeholder': 'Start typing here...',
    },
}




# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')