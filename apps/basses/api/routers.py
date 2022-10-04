from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from apps.basses.api.viewsets.bases_viewsets import *


router=DefaultRouter()
router.register(r'recibida',recibidaGTCViewSet,basename='endpoint recibida gtc')
router.register(r'enviar',enviarGTCViewSet,basename='endpoint enviar gtc')
urlpatterns= router.urls