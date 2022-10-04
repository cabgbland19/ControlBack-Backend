from datetime import datetime
from django.utils import timezone
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.userss.api.serializers import UserstokenSerializer
from django.contrib.sessions.models import Session


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
                    token.delete()
                    token= Token.objects.create(user=user)
                    return Response({
                        'token':token.key,
                        'username':user_serializer.data,
                        'message':'login successfully!'
                    })

            else:
                return Response({'mesagge':'not active'}, status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'mesagge':'not valid'})

class Logout (APIView):
    def post(self,request,  *args, **kwargs):
        try:

            token= request.GET.get('token')
            token= Token.objects.filter(key=token).first()
        
            if token:
                user=token.user
                all_sessions=Session.objects.filter(expire_date__gte =datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data= session.get_decoded().get('_auth_user_id')
                        if user.id == int(session_data):
                            session.delete()
                token.delete()
               

                return Response({'session_message':'all sessions removed','token_mesage':'token removed'})
            else:
                return Response({'error':'Not found with this credentials'},status=status.HTTP_406_NOT_ACCEPTABLE)

        except:
            return Response({'error':'token not found in request'})


            


