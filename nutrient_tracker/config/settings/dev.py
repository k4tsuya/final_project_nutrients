import environ

from .base import *

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))

SECRET_KEY = env.str("SECRET_KEY")

ALLOWED_HOSTS = ["127.0.0.1"]

# Database credentials
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PWD"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    },
}
AUTH_USER_MODEL = 'user_info.User'


# Session settings
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

SESSION_COOKIES_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIES_AGE = 300
