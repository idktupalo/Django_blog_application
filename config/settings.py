from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-&_0am7$3b$5rw25p@u2+zp3ubw(m^&m)(=i!++-y)&&em#!gr1'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Local
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3-d party
    "crispy_forms",
    "crispy_bootstrap5",

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    # New
    'blog.apps.BlogConfig',
    'accounts.apps.AccountsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'config.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static 
STATIC_URL = 'static/'
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')), )
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'

# Crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# All-auth config
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
ACCOUNT_LOGOUT_REDIRECT = 'blog:post_list'
LOGIN_REDIRECT_URL = 'blog:post_list'
LOGOUT_REDIRECT_URL = 'blog:post_list'

ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "VERIFIED_EMAIL": True
    },
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Email config
EMAIL_HOST = 'smtp.gmail.com' # SMTP - Simple Mail Transfer Protocol
EMAIL_HOST_USER = 'kostya.tupalo@gmail.com'
EMAIL_HOST_PASSWORD = 'xdmujbkcgitjmrew'
EMAIL_PORT = 587
EMAIL_USE_TLS = True # TLS - Transport Layer Security