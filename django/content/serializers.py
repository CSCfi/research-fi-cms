from rest_framework import serializers

from .models import Page, Shortcut

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'title_fi', 'title_sv', 'title_en', 'content_fi', 'content_sv', 'content_en')        

class ShortcutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shortcut
        fields = ('id', 'title_fi', 'title_sv', 'title_en', 'content_fi', 'content_sv', 'content_en', 'image', 'link')