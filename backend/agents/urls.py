# backend/agents/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AgentViewSet,
    TeamViewSet,
    TemplateViewSet,
    AvatarViewSet,
    AvailableAvatarsView,
    CurrentUserView,
    RegisterView
)

router = DefaultRouter()
router.register(r'agents', AgentViewSet, basename='agent')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'templates', TemplateViewSet, basename='template')
router.register(r'avatars', AvatarViewSet, basename='avatar')

urlpatterns = [
    path('auth/user/', CurrentUserView.as_view(), name='current_user'),
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('available_avatars/', AvailableAvatarsView.as_view(), name='available_avatars'),
    path('', include(router.urls)),
]
