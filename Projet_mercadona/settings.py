"""
Django settings for Projet_mercadona project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
<<<<<<< HEAD
import dj_database_url
import environ
from django.core.management.utils import get_random_secret_key
from imagekitio import ImageKit
=======
>>>>>>> deb99e6569ee3246687f75e57b26335889c71f4b

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', default=get_random_secret_key())
#The `DYNO` env var is set on Heroku CI, but it's not a real Heroku app, so we have to
# also explicitly exclude CI:
# https://devcenter.heroku.com/articles/heroku-ci#immutable-environment-variables
IS_HEROKU_APP = "DYNO" in os.environ and not "CI" in os.environ
# SECURITY WARNING: don't run with debug turned on in production!
if IS_HEROKU_APP:
    DEBUG = False
else:
    DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ['https://*.fly.dev']
=======

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


>>>>>>> deb99e6569ee3246687f75e57b26335889c71f4b
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
<<<<<<< HEAD
    'whitenoise.runserver_nostatic',
=======
>>>>>>> deb99e6569ee3246687f75e57b26335889c71f4b
    'django.contrib.staticfiles',
    'promo.apps.PromoConfig',
    'rest_framework',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
<<<<<<< HEAD
    'whitenoise.middleware.WhiteNoiseMiddleware',
=======
>>>>>>> deb99e6569ee3246687f75e57b26335889c71f4b
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Projet_mercadona.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': [BASE_DIR, 'promo/templates']
=======
        'DIRS': [BASE_DIR / 'templates']
>>>>>>> deb99e6569ee3246687f75e57b26335889c71f4b
        ,
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

<<<<<<< HEAD
WSGI_APPLICATION = 'Projet_mercadona.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# if DEBUG:
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
# else:
# DATABASES = {
#     'default': env.db()
#
# }

AUTH_USER_MODEL = 'promo.User'

# CSRF_COOKIE_SECURE = False
# SESSION_COOKIE_SECURE = False
=======

WSGI_APPLICATION = 'Projet_mercadona.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "Mercadona_DB",
        "USER": "postgres",
        "PASSWORD": "superposgres",
        "HOST": "127.0.0.1",
        "PORT": "5432"
    }
}

AUTH_USER_MODEL = 'promo.User'

#CSRF_COOKIE_SECURE = False
#SESSION_COOKIE_SECURE = False
>>>>>>> deb99e6569ee3246687f75e57b26335889c71f4b

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

<<<<<<< HEAD
=======

>>>>>>> deb99e6569ee3246687f75e57b26335889c71f4b
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Guyana'

USE_I18N = True

USE_TZ = True

<<<<<<< HEAD
=======

>>>>>>> deb99e6569ee3246687f75e57b26335889c71f4b
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
<<<<<<< HEAD
# STATICFILES_DIRS = BASE_DIR / "staticfiles"

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    # Enable WhiteNoise's GZip and Brotli compression of static assets:
    # https://whitenoise.readthedocs.io/en/latest/django.html#add-compression-and-caching-support
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
=======
STATICFILES_DIRS = [
os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
>>>>>>> deb99e6569ee3246687f75e57b26335889c71f4b

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
<<<<<<< HEAD

imagekit = ImageKit(
    public_key='public_JqHpBljMCPzQEgTZ61Yz++1LfKs=',
    private_key='private_LJ/YlRNoJAL8T7FAPZl/aNAw+qk=',
    url_endpoint = 'https://ik.imagekit.io/kpvotazbj'
)
listfiles = imagekit.list_files()
i = 0
LIST_FILES = []
for picture in listfiles.list:
    LIST_FILES.append(listfiles.list[i].name)
    i +=1
print(LIST_FILES)


=======
>>>>>>> deb99e6569ee3246687f75e57b26335889c71f4b
