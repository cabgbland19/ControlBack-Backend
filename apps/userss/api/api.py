import dataclasses
from sys import excepthook
from urllib import response
from xml.dom.minidom import Document
from django.urls import is_valid_path
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.userss.models import *
from apps.userss.api.serializers import *
from django.http import JsonResponse
import asyncio
import json


@api_view(['GET','POST'])
def management_user(request):

    if request.method== 'GET':
        
        users= User.objects.all()
        users_serializer= UsersSerializer(users,many = True)
        return Response(users_serializer.data)

    elif request.method== 'POST':
        user_serializer= UsersSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(user_serializer.errors)

@api_view(['GET','PUT'])
def management_user_detail(request,id):
    if request.method== 'GET':
        """ Hola"""
        users= User.objects.filter(id=id).first()
        users_serializer= UsersSerializer(users)
        return JsonResponse({'data':users_serializer.data})

    elif request.method=='PUT':
        users= User.objects.filter(id=id).first()
        users_serializer= UsersSerializer(users,data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data)
        else:
            return Response(users_serializer.errors)
    
