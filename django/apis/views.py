from rest_framework import viewsets

from content.models import Page, Shortcut
from content.serializers import PageSerializer, ShortcutSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class ShortcutViewSet(viewsets.ModelViewSet):
    queryset = Shortcut.objects.all()
    serializer_class = ShortcutSerializer