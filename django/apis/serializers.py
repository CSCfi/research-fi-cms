from rest_framework import serializers
from pages.models import Page
from shortcuts.models import Shortcut


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'title_fi', 'title_sv', 'title_en', 'content_fi', 'content_sv', 'content_en')

class ShortcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortcut
        fields = ('id', 'title_fi', 'title_sv', 'title_en', 'content_fi', 'content_sv', 'content_en', 'image', 'link')
