# backend/visual_agent/urls.py

from django.contrib import admin
from django.urls import path, include  # Убедитесь, что path импортирован
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('agents.urls')),  # Маршруты агента
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Добавляем маршруты для статических файлов и изображений в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Обслуживание изображений из frontend-next/public/images/
    urlpatterns += static('/images/', document_root=os.path.abspath(os.path.join(settings.BASE_DIR, '..', 'frontend-next', 'public', 'images')))
