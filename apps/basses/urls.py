from django.urls import path
from apps.basses.api.api import *


urlpatterns=[
   path('GTCrecibida/',BaseRecibidaGTC,name='GTCRecibidaApi'),
   path('GTCenviar/',BaseEnviarGTC,name='GTCenviarapi'),
]