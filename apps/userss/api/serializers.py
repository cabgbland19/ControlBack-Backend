from rest_framework import serializers
from apps.userss.models import *



class UserstokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','name','password')



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
