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

class BaseRecibidaGesUcsSerializer(serializers.ModelSerializer):
    class Meta:
        model=BaseRecibidaGesUcs
        fields='__all__'

class BaseEnviarGesUcsSerializer(serializers.ModelSerializer):
    class Meta:
        model=BaseEnviarGesUcs
        fields='__all__'

class RolsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Rols
        fields='__all__'

class CampaignSerializers(serializers.ModelSerializer):
    class Meta:
        model=Campaign
        fields='__all__'