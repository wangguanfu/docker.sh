# -*- coding: utf-8 -*-
"""
Django settings for mmcsite project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9x!*&^%y2rj%gaiw!wmbrzgnp*rr)k8$1v5us)1tni=^&e)95='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'device',
    'express',
    'order',
    'temperature',
    'event'
]


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users.middleware.rbac.RbacMiddleware',
]

ROOT_URLCONF = 'mmcsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'mmcsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     #'ENGINE': 'django.db.backends.sqlite3',
    #     #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'iot',
    #     'USER': 'root',
    #     'PASSWORD': 'Mmc,75022801',
    #     'HOST': '',
    #     'PORT': '',onpypyth
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'iot',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'mysql',
        # 'PASSWORD': '',
        'HOST':'mysql',
        'PORT':'3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# #
# AUTH_USER_MODEL = 'users.User'
############ 权限相关配置 ############
PERMISSION_URL_KEY = "LKfsaddHsLAJSdseJRQ"
PERMISSION_CODE_KEY = "MsdasLMSxkmsdaodapHl"
# URL白名单
VALID_URL_LIST = [
    '/admin/',
    '/users/login/',
    # '/users/post/',
    '/users/logout/',
    # '/favicon.ico/'
]
# login-URL
RBAC_LOGIN_URL = "/users/login/"


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


# Import production settings if the environment variable DJANGO_PRODUCTION is true
# (It's set to True by default in the Dockerfile, but you can override it with `docker run` for development)
if os.environ['DJANGO_PRODUCTION'] == 'true':
    from settings_production import *
