"""
Django settings for pythonathon_v3 project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3ds#)t0=6y97$qihq96u6=8^bmb*tmyc**fn92kds_#rf0-jg&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUGMODE', int(True))))

ALLOWED_HOSTS = ['localhost', 'pythonathon', 'nbproxy']
if 'VIRTUAL_HOST' in os.environ:
    ALLOWED_HOSTS += [h.strip() for h in os.environ['VIRTUAL_HOST'].split(',')]


# Application definition

INSTALLED_APPS = [
    'ctf.apps.CtfConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'oauth2_provider',
    'corsheaders',
    'graphene_django',
]

GRAPHENE = {
    'SCHEMA': 'pythonathon_v3.schema.schema'  # Where your Graphene schema lives
}

AUTHENTICATION_BACKENDS = [
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
]

ROOT_URLCONF = 'pythonathon_v3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                # 'account.context_processors.account',
                'ctf.context_processors.hubpath_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'pythonathon_v3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': 'postgres',
        'PASSWORD': open(os.environ.get('POSTGRES_PASSWORD_FILE', '/dev/null')).read().strip(),
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': '',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/profile'

# ACCOUNT_PASSWORD_USE_HISTORY = True
# ACCOUNT_PASSWORD_EXPIRY = 60*60*24*365  # one year


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_ROOT = os.environ.get('FILE_STORAGE', '')
MEDIA_URL = '/dl/'

MARKDOWN_EXTRAS = [
    'break-on-newline',
    'code-friendly',
    'fenced-code-blocks',
]

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
user_path = os.environ.get('GMAIL_USER_PATH', None)
if user_path and os.path.exists(user_path):
    EMAIL_HOST_USER = open(os.environ['GMAIL_USER_PATH']).read()
    EMAIL_HOST_PASSWORD = open(os.environ['GMAIL_PWD_PATH']).read()