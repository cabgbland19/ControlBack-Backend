from email import message
from rest_framework.authentication import get_authorization_header
from apps.userss.authentication import authtoken
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
class Authentication(object):
    user=None

    def get_user(self, request):
        token=  get_authorization_header(request).split()
        if token:
            try:
                token=token[1].decode()
                print(token)
            except:
                return None

            tokenauth=authtoken()
       
            user,token,message=tokenauth.authenticate_credentials(token)
            if user !=None and token !=None:
                return user
            return message
        return None
        
            

    def dispatch(self, request,*args, **kwargs):
            user=self.get_user(request)
            if user !=None:
                if type(user) == str:
                    response=Response({'error':user}, status=status.HTTP_401_UNAUTHORIZED)
                    response.accepted_renderer = JSONRenderer()
                    response.accepted_media_type = 'application/json'
                    response.renderer_context ={}
                    return response
                return super().dispatch(request, *args, **kwargs)
            response=Response({'error':'Error in credentials'},status=status.HTTP_400_BAD_REQUEST)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = 'application/json'
            response.renderer_context ={}
            return response


    
