#encoding:utf-8

# Identificando la ruta del proyecto
import os
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

#Configuraciones personalizadas

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

AUTH_USER_MODEL = 'usuarios.MyUser'

#Admin

ADMINS = (
('Jonathan Gonzalez', 'jgacosta@correo.com'),
)

#Ruta donde se guardan las imagenes
MEDIA_ROOT = os.path.join(RUTA_PROYECTO,'carga')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0h$rry4jd0+&oh6n+*q^xjz+c)m374q+e$kx3#z8&&+*avox$r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.sites',
'django.contrib.messages',
'django.contrib.staticfiles',
'django.contrib.admin',
'django.contrib.admindocs',
'tablas',
'usuarios',
'incidencias'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gestor.urls'

WSGI_APPLICATION = 'gestor.wsgi.application'

TEMPLATE_DIRS = (
     os.path.join(RUTA_PROYECTO,'plantillas'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
"django.core.context_processors.request"
)

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql', 
'NAME': 'gestor', 
'USER': 'root', 
'PASSWORD': '', 
'HOST': '', 
'PORT': '', 
}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
     os.path.join(RUTA_PROYECTO,'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SITE_ID = 1