from django.urls import path

from .views import (
    PageViewSet,
    ShortcutViewSet,
    FigureViewSet,
    SectorViewSet,
    ExternalLinkViewSet,
    MyDataViewSet,
)
from rest_framework.routers import DefaultRouter

# Default router lists views
router = DefaultRouter()
router.register(r"pages", PageViewSet)
router.register(r"shortcuts", ShortcutViewSet)
router.register(r"figures", FigureViewSet)
router.register(r"sectors", SectorViewSet)
router.register(r"external_links", ExternalLinkViewSet)
router.register(r"mydata", MyDataViewSet)
urlpatterns = router.urls
