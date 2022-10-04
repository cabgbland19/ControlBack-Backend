from datetime import timedelta
from email import message
from multiprocessing import AuthenticationError
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone
from django.conf import settings

class authtoken(TokenAuthentication):

    def authenticate_credentials(self,key):
        message,token,user=None,None,None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            user = token.user
        except self.get_model().DoesNotExist:
        
            message='Invalid token'
            
        if token is not None:

            if not token.user.is_active:
                message='Inactive user'

        return(user,token,message)