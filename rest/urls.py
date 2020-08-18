from django.urls import path, include
from rest_framework import routers

from .views import PermissionViewSet, GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'permissions', PermissionViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    # AUTH 0 authentication
    path('auth0/', include('rest_auth.urls')),

    # OAUTH 2 authentication
    path('auth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # Rest Framework API support Browsable API
    path('', include(router.urls)),

    # Rest Framework Auth support Browsable API
    path('', include('rest_framework.urls', namespace='rest_framework')),
]
