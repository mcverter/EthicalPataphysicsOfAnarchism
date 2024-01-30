"""
Django settings for django_backend project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

# from word_analysis.templatetags.radical_empiricism_templates import french_english
from pathlib import Path

from constants import DB_NAME, DB_PORT, DB_RUNTIME_USER, DB_RUNTIME_PASSWORD, DB_RUNTIME_HOST, \
    DB_ENGINE, DB_LEVEL

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zy_@((2m@f1*vlp0otae4+-!j%!fnszx2+&h--l$$-q#upr@$l'

# SECURITY WARNING: don't run with debug turned on in production!
if DB_LEVEL == 'local':
    DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost',
                 'levinas-radical-empiricism-aa0fc6fe9dbc.herokuapp.com',
                 'levinasradicalempiricism.com',
                 'levinas-empirisme-radical-56386a1e25f9.herokuapp.com',
                 'levinasempirismeradical.com',
                 'levinasempirismeradical.fr',
                 'levinas-empirisme-radical-ab15e29ab349.herokuapp.com'
                 ]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "word_analysis",
    'corsheaders',
    'django_sass',
    'livereload'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = 'django_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'word_analysis/content'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'word_analysis.context_processors.title_context',
                'word_analysis.context_processors.messages_context',
            ],
            'builtins': ['word_analysis.templatetags.radical_empiricism_templates'],
        },
    },
]

WSGI_APPLICATION = 'django_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        "ENGINE": DB_ENGINE,
        'NAME': DB_NAME,
        'USER': DB_RUNTIME_USER,
        'PASSWORD': DB_RUNTIME_PASSWORD,
        'HOST': DB_RUNTIME_HOST,
        'PORT': DB_PORT,
        'OPTIONS': {'sslmode': 'require'}
    }
}

# Use SSL for remote connection
if DB_LEVEL != 'local':
    DATABASES["default"]['OPTIONS']: {'sslmode': 'require'}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000'
]
