from django.urls import path

from .views import PostViewSet, ShortcutViewSet, FigureViewSet, SectorViewSet
from rest_framework.routers import DefaultRouter

# Default router lists views
router = DefaultRouter()
router.register(r'pages', PostViewSet)
router.register(r'shortcuts', ShortcutViewSet)
router.register(r'figures', FigureViewSet)
router.register(r'sectors', SectorViewSet)
urlpatterns = router.urls