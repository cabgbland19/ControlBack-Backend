from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from apps.userss.api.serializers import UserstokenSerializer


class Login (ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer= self.serializer_class(data=request.data, context={'request':request})
        if login_serializer.is_valid():
            user=login_serializer.validated_data['user']
            if user.is_active:
                token,created=Token.objects.get_or_create(user=user)
                user_serializer= UserstokenSerializer(user)
                if created:
                    return Response({
                        'token':token.key,
                        'username':user_serializer.data,
                        'message':'login successfully!'
                    })
            else:
                return Response({'mesagge':'not active'}, status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'mesagge':'not valid'})

            


