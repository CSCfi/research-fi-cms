from rest_framework import serializers

from .models import Shortcut

class ShortcutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shortcut
        fields = ('title_fi', 'title_sv', 'title_en', 'content_fi', 'content_sv', 'content_en')