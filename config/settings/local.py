from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'progmatchdb',  
        'USER': 'admin',  
        'PASSWORD': 'cPHeYJa4r3f4UTecvOVDN36SDHaft26B',
        'HOST': '35.227.164.209',  
        'PORT': '5432', 
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'presentation/UI/staticFiles/'
STATICFILES_DIRS = [STATIC_URL]