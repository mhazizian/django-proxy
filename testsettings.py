
DEBUG = False

ALLOWED_HOSTS = [
    '195.201.13.227',
    '82.102.12.207',
    '82.102.12.207:8080',
    '94.182.227.193',
    '99.91.97.238',
    'hamclassy-test',
    'backend.hamclassy.ir'
]

SECRET_KEY = '12345'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'proxy',
)
