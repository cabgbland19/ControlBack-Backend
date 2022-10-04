from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from apps.userss.api.viewsets.user_viewset import UserViewSet

router=DefaultRouter()

router.register(r'user',UserViewSet,basename='endpoint users')

urlpatterns= router.urls