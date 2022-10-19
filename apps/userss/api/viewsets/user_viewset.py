from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from apps.userss.authentication_mixin  import Authentication
from apps.userss.api.serializers import UsersSerializer,UpdateUserSerializer,UpdateUserPswdSerializer,UsersCreateSerializer
from apps.basses.api.serializers import RolsSerializers, CampaignSerializers
from apps.userss.api.serializers import UserRegisterSerializer
from django.shortcuts import get_object_or_404
from apps.userss.models import User
from apps.basses.models import Rols, Campaign

class UserViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class= UsersSerializer
    serializer_class2= RolsSerializers
    serializer_class3= UpdateUserSerializer
    serializer_class4= UpdateUserPswdSerializer
    serializer_class5= UsersCreateSerializer
    parser_classes=(JSONParser,MultiPartParser)
    model = User
    model2 = Rols

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active=True)


    def list(self, request):
        user_serializer = self.get_serializer(self.get_queryset(), many=True)
        data={}
       
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": user_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        # send information to serializer 
        data={}

        for i in request.data.items():
            var=i[0]
            data[var]=i[1]


        id_rol=request.data['id_rol']
        rol= Rols.objects.filter(id=id_rol).first()
        rol_serializer= RolsSerializers(rol)
        data['rol']=str(rol_serializer.data['spanish_name'])

                

        id_campaign=request.data['cost_center']
        campaign= Campaign.objects.filter(id=id_campaign).first()
        campaign_serializer= CampaignSerializers(campaign)
        data['campaign']=str(campaign_serializer.data['name'])



        serializer = self.serializer_class5(data=data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created succesfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def retrieve(self,request,pk):
        user = self.get_object(pk)
        

    def update(self, request, pk=None):
        user = self.get_object(pk)
        data={}


        id_rol=request.data['id_rol']
        for i in request.data.items():
            var=i[0]
            data[var]=i[1]


        rol= Rols.objects.filter(id=id_rol).first()
        rol_serializer= RolsSerializers(rol)
        data['rol']=str(rol_serializer.data['spanish_name'])

        id_campaign=request.data['cost_center']
        campaign= Campaign.objects.filter(id=id_campaign).first()
        campaign_serializer= CampaignSerializers(campaign)
        data['campaign']=str(campaign_serializer.data['name'])
    
        if 'password' in data:
             user_serializer = self.serializer_class4(user, data=data)
        else:
             
            user_serializer = self.serializer_class3(user, data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'User updated successfully'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'error',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


