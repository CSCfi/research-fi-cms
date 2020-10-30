from rest_framework import viewsets

from contentapp.models import Page, Shortcut, Figure
from contentapp.serializers import PageSerializer, ShortcutSerializer, FigureSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class ShortcutViewSet(viewsets.ModelViewSet):
    queryset = Shortcut.objects.all()
    serializer_class = ShortcutSerializer

class FigureViewSet(viewsets.ModelViewSet):
    queryset = Figure.objects.all()
    serializer_class = FigureSerializer