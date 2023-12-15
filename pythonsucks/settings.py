import os
from os.path import abspath, dirname

from ckeditor.configs import DEFAULT_CONFIG
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / "subdir".
PROJECT_DIR = abspath(dirname(__file__))
REPO_DIR = dirname(PROJECT_DIR)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = os.getenv("DEBUG", False)

ALLOWED_HOSTS = ["localhost", "blog.storv.us"]


def root(x):
    return abspath(os.path.join(PROJECT_DIR, x))


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pythonsucks.article",
    "ckeditor",
    "taggit",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pythonsucks.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pythonsucks.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = (
    root("static"),
    os.path.join(REPO_DIR, 'static/'),
)
STATIC_ROOT = "/var/www/html/static"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CUSTOM_TOOLBAR = [
    {
        "name": "document",
        "items": [
            "Styles",
            "Format",
            "Bold",
            "Italic",
            "Underline",
            "Strike",
            "-",
            "TextColor",
            "BGColor",
            "-",
            "JustifyLeft",
            "JustifyCenter",
            "JustifyRight",
            "JustifyBlock",
        ],
    },
    {'name': 'forms',
     'items': ['Form', 'Checkbox']},
    {
        "name": "widgets",
        "items": [
            "Undo",
            "Redo",
            "-",
            "NumberedList",
            "BulletedList",
            "-",
            "Outdent",
            "Indent",
            "-",
            "Link",
            "Unlink",
            "-",
            "Image",
            "CodeSnippet",
            "Table",
            "HorizontalRule",
            "Smiley",
            "SpecialChar",
            "-",
            "Blockquote",
            "-",
            "ShowBlocks",
            "Maximize",
        ],
    },
]


CKEDITOR_CONFIGS = {
    "default": {
        "skin": "moono-lisa",
        "toolbar": CUSTOM_TOOLBAR,
        "toolbarGroups": None,
        "extraPlugins": ",".join(["image2", "codesnippet"]),
        "removePlugins": ",".join(["image"]),
        "codeSnippet_theme": "xcode",
    },
}

TAGGIT_CASE_INSENSITIVE = True
