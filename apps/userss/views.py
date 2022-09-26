from tokenize import Token
from urllib import response
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class Login(ObtainAuthToken):

    def post(self,request,*arg,**kwargs):
        login_serializer=self.serializer_class(data=request.data,context={'request':request})
        if login_serializer.is_valid():
           user=login_serializer.validated_data['user']
           token,created= Token.objects.get_or_create(user=user)

        else:
            return Response({
                'message':'Not valid'
            })
            


