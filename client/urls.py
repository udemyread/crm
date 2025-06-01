from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ClientViewSet, OrderViewSet, InteractionViewSet, RegisterView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# API routers
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)    # Bu yerda stats endpoint avtomatik hosil bo'ladi
router.register(r'orders', OrderViewSet)
router.register(r'interactions', InteractionViewSet)

# Swagger schema
schema_view = get_schema_view(
    openapi.Info(
        title="CRM API",
        default_version='v1',
        description="CRM tizimi uchun API hujjatlari",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your@email.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),   # router ichida /clients/stats/ ham bo'ladi
    path('api/signup/', RegisterView.as_view(), name='signup'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger & ReDoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
