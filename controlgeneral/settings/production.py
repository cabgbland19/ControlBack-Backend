from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME':'controlback',
        'USER': '',
        'PASSWORD':'',
        'HOST': 'U27TEC01\SQLEXPRESS',
        'PORT':'',
        'OPTIONS':{
            "driver":'ODBC Driver 17 for SQL Server'
        },
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':'controlback',
#         'USER': 'root',
#         'PASSWORD':'',
#         'HOST': 'localhost',
#         'PORT':'3306'
#     }
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'