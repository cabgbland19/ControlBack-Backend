import dataclasses
from sys import excepthook
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.basses.models import *
from apps.basses.api.serializers import *
from django.http import JsonResponse
import asyncio
import json
from rest_framework.decorators import api_view
from apps.userss.authentication_mixin import Authentication

@api_view(['GET'])   
def BaseRecibidaGTC(request):

        if request.method== 'GET':
            baserecibida= BaseRecibidaGtc.objects.all()
            baserecibida_serializer= BaserecibidaGTCserializer(baserecibida,many=True)
            data=baserecibida_serializer.data
            
            return Response({ 
                "response":data
                }
            )
@api_view(['GET','POST','PUT'])
def BaseEnviarGTC(request):
    if request.method== 'GET':
        Authentication()
        baseenviar= BaseEnviarGtc.objects.all()
        baseenviar_serializer=BaseenviarGTCserializer(baseenviar,many=True)
        data=baseenviar_serializer.data
        print(data)
        return Response({ 
        "response":data
        })
    elif request.method=='POST':
        Authentication()
        base_enviar_gtc= BaseenviarGTCserializer(data=request.data)
        if base_enviar_gtc.is_valid():
            base_enviar_gtc.save()
            return Response(base_enviar_gtc.data)
        else:
            return Response(base_enviar_gtc.errors)