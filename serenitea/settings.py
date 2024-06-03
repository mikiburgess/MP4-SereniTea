"""
MILESTONE PROJECT 4 by MIKHAILA BURGESS
Django settings for "SERENITEA EMPORIUM"
    using Django 4.2.13.
- - - - - - - - - - - - - - - - - - - -
"""

from pathlib import Path
from decimal import Decimal
import os
import dj_database_url

# import environment variables from env.py, if present
if os.path.exists("env.py"):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")

ALLOWED_HOSTS = [
    'mp4-serenitea-emporium-5454dc22e46f.herokuapp.com',
    '127.0.0.1',
    'localhost',
]


# Application definition

INSTALLED_APPS = [
    # Use WhiteNoise's runserver implementation instead of the Django default,
    "whitenoise.runserver_nostatic",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # The following apps are required by allauth:
    'django.contrib.sites',
    'allauth',  # allauth itself
    'allauth.account',  # app that allows basic user accounts

    # Additional third-party apps
    'crispy_forms',
    'crispy_bootstrap5',
    'storages',

    # Project-specific apps
    'home',
    'products',
    'basket',
    'checkout',
    'profiles',

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
    # allauth account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'serenitea.urls'

# Crispy forms template packs
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                # to make shopping basket accessible across all apps
                'basket.contexts.basket_contents',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# AUTHENTICATION_BACKENDS - copied from https://docs.allauth.org/en/latest/installation/quickstart.html
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Email details
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

# Settings for allauth account authentication
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # allow login using username or email
ACCOUNT_EMAIL_REQUIRED = True  # users must register with an email address
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # registration only confirmed upon email verification
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True  # Enter email twice on registration to ensure it's correct
ACCOUNT_USERNAME_MIN_LENGTH = 4  # minimum allowed username length
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'SereniTea - '  # Email subject prefix text
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1  # num days email invite becomes invalid
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True  # automatically log in user upon email authentication
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True  # automatically log in user upon password reset
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'  # upon login, redirect to front page of store/site
WSGI_APPLICATION = 'serenitea.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# WITHOUT AWS
STATIC_URL = '/static/'
STATICFILESDIRECT_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_URL = '/media/'
PRODUCT_IMAGES = os.path.join(MEDIA_URL, 'products/')
SITE_IMAGES = os.path.join(MEDIA_URL, 'images/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Session Cookies
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # session details deleted on browser close
SESSION_COOKIE_AGE = 3600 # sessionid cookie expire after 1 hour

# Shipping cost data
FREE_DELIVERY_THRESHOLD = Decimal('30.00')
STANDARD_DELIVERY_CHARGE = Decimal('5.99')

# Load Stripe data
STRIPE_CURRENCY = 'gbp'
STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_WH_SECRET = os.environ.get("STRIPE_WH_SECRET")

# For Whitenoise
STATIC_ROOT = BASE_DIR / "staticfiles"

# For Whitenoise
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    # Enable WhiteNoise's GZip and Brotli compression of static assets:
    # https://whitenoise.readthedocs.io/en/latest/django.html#add-compression-and-caching-support
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Don't store the original (un-hashed filename) version of static files, to reduce slug size:
# https://whitenoise.readthedocs.io/en/latest/django.html#WHITENOISE_KEEP_ONLY_HASHED_FILES
WHITENOISE_KEEP_ONLY_HASHED_FILES = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
