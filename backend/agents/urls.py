# backend/agents/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, TeamViewSet, RegisterView

router = DefaultRouter()
router.register(r'agents', AgentViewSet, basename='agent')
router.register(r'teams', TeamViewSet, basename='team')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),  # Добавляем маршрут для регистрации
]
