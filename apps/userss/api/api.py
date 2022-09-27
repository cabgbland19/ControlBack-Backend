import dataclasses
from sys import excepthook
from urllib import response
from xml.dom.minidom import Document
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.userss.models import *
from apps.userss.api.serializers import *
from django.http import JsonResponse
import asyncio
import json




class UsersAPIVIEW(APIView):


    def get(self,request):
            registereduser= User.objects.all()
            registereduser_serializer=UsersSerializer(registereduser,many=True)
            data=registereduser_serializer.data
            return Response({ 
            "response":data
            })

    def post(self,request):
        try:
            document=request.data['document']
            password=request.data['password']
            campaign=request.data['campaign']
            id_rol=request.data['id_rol']

            registeruser=User(
                document=document,
                password=password,
                campaign=campaign,
                id_rol=id_rol,
            )
            registeruser.save()
            return Response({
                    "status":"true",
                    "message":"Se guardó"

                })
        except BaseException as err:
                return Response({
                    "status":"true",
                    "message":" No se guardó",
                    "OS error": type(err),
                    "test": "test"
                })
    def getById(request,id):

            registereduser= User.objects.filter(id=id)
            registereduser_serializer=UsersSerializer(registereduser,many=True)
            data=registereduser_serializer.data
            if len(data) > 0:
                print(type(data))
                return JsonResponse({
                    "status": "true",
                    "message": "Se ha encontrado con éxito",
                    "response": data})
                    
            else:
                return JsonResponse({
                    "status": "true",
                    "messege": "No se encontraron registros",
                    "response": []
                })

