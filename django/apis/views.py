from rest_framework import viewsets

from contentapp.models import Page, Shortcut, Figure, Sector, ExternalLinksParent
from contentapp.serializers import (
    PageSerializer,
    ShortcutSerializer,
    FigureSerializer,
    SectorSerializer,
    ExternalLinksParentSerializer,
)


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class ShortcutViewSet(viewsets.ModelViewSet):
    queryset = Shortcut.objects.all()
    serializer_class = ShortcutSerializer


class FigureViewSet(viewsets.ModelViewSet):
    queryset = Figure.objects.all()
    serializer_class = FigureSerializer


class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


class ExternalLinkViewSet(viewsets.ModelViewSet):
    queryset = ExternalLinksParent.objects.all()
    serializer_class = ExternalLinksParentSerializer