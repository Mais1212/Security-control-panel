import os

from environs import Env


environment = Env()
environment.read_env()

DATABASES = {
    "default": {
        "ENGINE": environment("ENGINE"),
        "HOST": environment("HOST"),
        "PORT": environment("PORT"),
        "NAME": environment("NAME"),
        "USER": environment("USER"),
        "PASSWORD": environment("PASSWORD"),
    }
}

INSTALLED_APPS = ["datacenter"]

SECRET_KEY = environment("SECRET_KEY")

DEBUG = environment.bool("DEBUG", False)

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ["*"]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
    },
]


USE_L10N = True

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_TZ = True
