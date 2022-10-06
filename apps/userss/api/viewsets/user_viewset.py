from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from apps.userss.authentication_mixin  import Authentication
from apps.userss.api.serializers import UsersSerializer
from apps.userss.api.serializers import UserRegisterSerializer

class UserViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class= UsersSerializer
    parser_classes=(JSONParser,MultiPartParser)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active=True)
    def list(self, request):
        user_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": user_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        # send information to serializer 
       
        serializer = self.serializer_class(data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created succesfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            
            user_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({'message':'User updated succesfully!','data':user_serializer.data}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

