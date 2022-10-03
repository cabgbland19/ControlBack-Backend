from rest_framework import serializers
from apps.basses.models import *

class BaserecibidaGTCserializer(serializers.ModelSerializer):
    class Meta:
        model=BaseRecibidaGtc
        fields='__all__'

class BaseenviarGTCserializer(serializers.ModelSerializer):
    class Meta:
        model=BaseEnviarGtc
        fields='__all__'
