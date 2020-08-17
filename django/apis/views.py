from rest_framework import viewsets

from pages.models import Page
from shortcuts.models import Shortcut
from .serializers import PageSerializer
from .serializers import ShortcutSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class ShortcutViewSet(viewsets.ModelViewSet):
    queryset = Shortcut.objects.all()
    serializer_class = ShortcutSerializer