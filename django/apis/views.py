from rest_framework import viewsets

from contentapp.models import Page, Shortcut
from contentapp.serializers import PageSerializer, ShortcutSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class ShortcutViewSet(viewsets.ModelViewSet):
    queryset = Shortcut.objects.all()
    serializer_class = ShortcutSerializer