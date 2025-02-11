"""
Django settings for BD2_Trabalhofinal project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--lv!u*3%v6b-j7pw6$xb9id6xc_^%prj!2rhb#$8d2=*lco$w3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    'BD2_Trabalhofinal.App',  # Certifique-se de que este é o caminho correto
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
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

ROOT_URLCONF = 'BD2_Trabalhofinal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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





WSGI_APPLICATION = 'BD2_Trabalhofinal.wsgi.application'





# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases



DATABASES = {
    # postgreSQL => Utilizadores
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'projeto_BD2',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    #mongoDB => Resto da Base de Dados
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'projeto_BD2',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
        },
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propagate': False,
                }
            },
        },
    },
}




# Adicione isto para gerenciar as rotas de database
DATABASE_ROUTERS = ['BD2_Trabalhofinal.App.routers.AuthRouter']




# settings.py
AUTHENTICATION_BACKENDS = [
    'BD2_Trabalhofinal.App.authentication_backend.CustomAuthBackend',  # Adiciona seu backend personalizado aqui
    'django.contrib.auth.backends.ModelBackend',  # O backend padrão também pode ser mantido, se necessário
]


DATABASE_ROUTERS = ['BD2_Trabalhofinal.App.routers.MultiDBRouter']




# Backend de sessão
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Usa banco de dados para sessões



# Opcional: tempo de duração da sessão (em segundos)
SESSION_COOKIE_AGE = 1209600  # 2 semanas



# Permitir que a sessão termine ao fechar o navegador (se necessário)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True



# Domínio do cookie (se você estiver usando subdomínios, isso pode ser necessário)
SESSION_COOKIE_DOMAIN = None



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





AUTH_USER_MODEL = 'App.Utilizador'  # Substitui 'tua_app' pelo nome da tua app





ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.81']


