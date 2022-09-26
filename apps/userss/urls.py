from django.urls import path
# from . import views
# from api import *
from apps.userss.api.api import *


urlpatterns=[

   path('GTCrecibida/',BaserecibidaAPIVIEW.as_view(),name='GTCRecibidaApi'),
   path('GTCenviar/',BaseEnviarAPIVIEW.as_view(),name='GTCenviarapi'),
   path('user/',UsersAPIVIEW.as_view(),name='useruserapi'),
   path('user/<int:document>/',UsersAPIVIEW.getByDocument,name='userapibyid'),
   


]