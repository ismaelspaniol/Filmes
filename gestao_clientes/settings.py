import os, sys
from dj_database_url import parse
from decouple import config


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_DIR = os.path.join(BASE_DIR, os.pardir)

TENANT_APPS_DIR = os.path.join(PROJECT_DIR, os.pardir)
sys.path.insert(0, TENANT_APPS_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['gestao-clientes3550.herokuapp.com', 'localhost', 'tenant1.trendy-sass.com', 'tenant2.trendy-sass.com',
                 'sulinotenant.com']


SITE_ID = 1

# Application definition


MIDDLEWARE = [
    'gestao_clientes.middleware.TenantTutorialMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestao_clientes.urls_tenants'
PUBLIC_SCHEMA_URLCONF = 'gestao_clientes.urls_public'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',

            ],
        },
    },
]

WSGI_APPLICATION = 'gestao_clientes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# ///para usar o sqlite3, quando estiver trabalhando local
# default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
# DATABASES = {
#     'default': {
#         "ENGINE": "django_tenants.postgresql_backend",
#         'NAME': 'sincroniza_rh',                      # Or path to database file if using sqlite3.
#         'USER': 'postgres',
#         'PASSWORD': 'masterkey',
#         'HOST': 'localhost',   # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#         'PORT': '5433',            # Set to empty string for default.
#     }
# }

default_dburl = 'postgres://postgres:masterkey@localhost:5433/sincroniza_rh'
#db heroku  d1b1lk04m60jga
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=parse),
}

DATABASES['default']['ENGINE'] = 'django_tenants.postgresql_backend'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = 'media'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = 'clientes:persons_list'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    'statics',
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'


SHARED_APPS = (
    'django_tenants',  # mandatory
    'customers',  # you must list the app where your tenant model resides in

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

)

TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'bootstrapform',
    'clientes',
    'home',
    'pages',
    'empresa',
    'ferias',
    'movies',
    'musicas',
)

TENANT_MODEL = "customers.Client"  # app.Model

TENANT_DOMAIN_MODEL = "customers.Domain"  # app.Model

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

INSTALLED_APPS = list(set(TENANT_APPS + SHARED_APPS))


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

DATE_FORMAT = 'd/m/Y'

DATE_INPUT_FORMATS = (
    '%d/%m/%Y',
)

