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



class BaserecibidaAPIVIEW(APIView):
    
    def get(self,request):
        baserecibida= BaseRecibidaGtc.objects.all()
        baserecibida_serializer= BaserecibidaGTCserializer(baserecibida,many=True)
        data=baserecibida_serializer.data
        
        return Response({ 
            "response":data
            }
        )

class BaseEnviarAPIVIEW(APIView):
    
        def get(self,request):
            baseenviar= BaseEnviarGtc.objects.all()
            baseenviar_serializer=BaseenviarGTCserializer(baseenviar,many=True)
            data=baseenviar_serializer.data
            print(data)
            return Response({ 
            "response":data
            })

        def post(self,request):
            try:
                cuenta=request.data['cuenta']
                contacto=request.data['contacto']
                gtcaplica=request.data['gtcaplica']
                tipo_solucion=request.data['tipo_solucion']
                motivo_gtc=request.data['motivo_gtc']
                campo_observacion=request.data['campo_observacion']
                valor_diferencial=request.data['valor_diferencial']
                marcacion=request.data['marcacion']
                solucionado=request.data['solucionado']
                informacion=request.data['informacion']
                fecha_solcionado=request.data['fecha_solcionado']
                gestor=request.data['gestor']
                valor_mensual=request.data['valor_mensual']
                meses_ajuste=request.data['meses_ajuste']
                id_llamada=request.data['id_llamada']
                usuario_de_red=request.data['usuario_de_red']
                nombre_asesor=request.data['nombre_asesor']
                team_leader=request.data['team_leader']
                gerente=request.data['gerente']

                baseenviar=BaseEnviarGtc(
                    cuenta=cuenta,
                    contacto=contacto,
                    gtcaplica=gtcaplica,
                    tipo_solucion=tipo_solucion,
                    motivo_gtc=motivo_gtc,
                    campo_observacion=campo_observacion,
                    valor_diferencial=valor_diferencial,
                    marcacion=marcacion,
                    solucionado=solucionado,
                    informacion=informacion,
                    fecha_solcionado=fecha_solcionado,
                    gestor=gestor,
                    valor_mensual=valor_mensual,
                    meses_ajuste=meses_ajuste,
                    id_llamada=id_llamada,
                    usuario_de_red=usuario_de_red,
                    nombre_asesor=nombre_asesor,
                    team_leader=team_leader,
                    gerente=gerente,
                )
                baseenviar.save()
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

class UsersAPIVIEW(APIView):


    def get(self,request):
            registereduser= users.objects.all()
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

            registeruser=users(
                document=document,
                password=password,
                campaign=campaign,
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
    def getByDocument(request,document):

            registereduser= users.objects.filter(document=document)
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

class UsersloginAPIVIEW(APIView):


     def post(self,request):
        try:
            document=request.data['document']
            password=request.data['password']


            
            response= json.dumps(UsersAPIVIEW.getByDocument(document))

            


            # docu=response.data['document']

            if len(response) > 0:
                return Response({
                    "status": "true",
                    "message": "Se ha encontrado con éxito",
                    "response": response
                    })
                    
            else:
                return JsonResponse({
                    "status": "true",
                    "messege": "No se encontraron registros",
                    "response": []
                })
        except BaseException as err:
                return Response({
                    "status":"true",
                    "message":" No se guardó",
                    "OS error": type(err),
                    "test": "test"
                })
