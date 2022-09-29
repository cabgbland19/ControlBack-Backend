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

    def create(self, validated_data):
        user=User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        updated_user= super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
