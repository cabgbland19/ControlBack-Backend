from django.urls import path
# from . import views
# from api import *
from apps.userss.api.api import *


urlpatterns=[

   path('GTCrecibida/',BaserecibidaAPIVIEW.as_view(),name='GTCRecibidaApi'),
   path('GTCenviar/',BaseEnviarAPIVIEW.as_view(),name='GTCenviarapi'),
   path('login/<int:document>/',UsersAPIVIEW.getByDocument,name='loginuserapibyid'),
   path('login',UsersAPIVIEW.as_view,name='loginuserapi'),
   path('login/validation/', UsersloginAPIVIEW.as_view(),name='loginuser'),


]