from rest_framework import serializers

from .models import Page

class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ('title_fi', 'title_sv', 'title_en', 'content_fi', 'content_sv', 'content_en')