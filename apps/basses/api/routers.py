from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from apps.basses.api.viewsets.bases_viewsets import *


router=DefaultRouter()
router.register(r'recibida/gtc',recibidaGTCViewSet,basename='endpoint recibida gtc')
router.register(r'enviar/gtc',enviarGTCViewSet,basename='endpoint enviar gtc')
router.register(r'recibida/gesucs',recibidaGesUcsViewset,basename='endpoint recibida gesucs')
router.register(r'enviar/gesucs',enviarGesUcsViewset,basename='endpoint enviar gesucs')
urlpatterns= router.urls