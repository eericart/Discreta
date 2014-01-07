"""
Django settings for Discreta project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ofz9898ns97tc@mi*ob665a#^r1=$cq*3ejt_!z1l&q^kua+*b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Home',
    'django.contrib.admin',
    'south',
    'storages',
    'account',
    'bootstrap3',


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Discreta.urls'

WSGI_APPLICATION = 'Discreta.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates'),
)

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

CRISPY_TEMPLATE_PACK = 'bootstrap3'



# Parse database configuration from $DATABASE_URL
import dj_database_url
try :
    DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}
except Exception:
    pass

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
#User profile

AUTH_PROFILE_MODULE = 'account.UserProfile'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(os.path.abspath(os.path.dirname(__file__) + '/..'), 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# E-mail SERVER (Gmail)
ACCOUNT_ACTIVATION_DAYS=7
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'logicahire@gmail.com'
EMAIL_HOST_PASSWORD = 'hirelogica'
EMAIL_USE_TLS = True

AUTHENTICATION_BACKENDS = (
    'account.backend.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

try:
    from local_settings import *
except ImportError:
    pass