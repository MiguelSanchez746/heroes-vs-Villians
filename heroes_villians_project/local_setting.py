# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@y6*4rp4l-7&djw0e&qd6#yf&9ztw!78cngc1zd-a*+kx@w=-='


 #Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_villians_database',
        'HOSE': 'localhost',
        'USER': 'root',
        'PASSWORD': '91_Bravo746'
    }
}

