from django.urls import path

from .views import PostViewSet, ShortcutViewSet, FigureViewSet
from rest_framework.routers import DefaultRouter

# Default router lists views
router = DefaultRouter()
router.register(r'pages', PostViewSet)
router.register(r'shortcuts', ShortcutViewSet)
router.register(r'figure', FigureViewSet)
urlpatterns = router.urls