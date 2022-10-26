from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from apps.userss.api.viewsets.user_viewset import UserViewSet,UserbreakViewSet

router=DefaultRouter()

router.register(r'user',UserViewSet,basename='endpoint users')
router.register(r'breakuser',UserbreakViewSet,basename='endpoint break users')

urlpatterns= router.urls