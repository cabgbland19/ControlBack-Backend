from django.urls import path
# from . import views
# from api import *
from apps.userss.api.api import *


urlpatterns=[
   path('user/',UsersAPIVIEW.as_view(),name='useruserapi'),
   path('user/<int:document>/',UsersAPIVIEW.getById,name='userapibyid'),
   


]