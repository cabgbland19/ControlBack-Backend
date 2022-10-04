from django.urls import path
# from . import views
# from api import *
from apps.userss.api.api import *


urlpatterns=[
   path('user/',management_user,name='useruserapi'),
   path('user/<int:id>/',management_user_detail,name='detail'),
]