from django.urls import path

from .views import PostViewSet, ShortcutViewSet
from rest_framework.routers import DefaultRouter

# Default router lists views
router = DefaultRouter()
router.register(r'pages', PostViewSet)
router.register(r'shortcuts', ShortcutViewSet)
urlpatterns = router.urls