from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from apps.userss.authentication_mixin  import Authentication
from apps.basses.api.serializers import *


class recibidaGTCViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class= BaserecibidaGTCserializer
    parser_classes=(JSONParser,MultiPartParser)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.order_by('fecha_gtc')

    def list(self, request):
        gtcrecibida_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": gtcrecibida_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        # send information to serializer 
       
        serializer = self.serializer_class(data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'base field created succesfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class enviarGTCViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class= BaseenviarGTCserializer
    parser_classes=(JSONParser,MultiPartParser)
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.order_by('cuenta')

    def list(self, request):
        gtcenviar_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": gtcenviar_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    def create(self, request):
        # send information to serializer 
       
        serializer = self.serializer_class(data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'base field created succesfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            
            enviargtc_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if enviargtc_serializer.is_valid():
                enviargtc_serializer.save()
                return Response({'message':'Base updated succesfully!','data':enviargtc_serializer.data}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':enviargtc_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
