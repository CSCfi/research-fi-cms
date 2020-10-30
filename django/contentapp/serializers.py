from rest_framework import serializers

from .models import Page, Shortcut, Figure, SingleFigure

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('placement_id', 'title_fi', 'title_sv', 'title_en', 'content_fi', 'content_sv', 'content_en')        

class ShortcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortcut
        fields = ['placement_id', 'title_fi', 'title_sv', 'title_en', 'content_fi', 'content_sv', 'content_en', 'image', 'link']

class SingleFigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleFigure
        fields = ['placement_id', 'title_fi', 'title_sv', 'title_en', 'description_fi', 'description_sv', 'description_en', 'thumbnail', 'iframe_fi', 'iframe_sv', 'iframe_en',
        'link_id', 'source_fi', 'source_sv', 'source_en', 'info_fi', 'info_sv', 'info_en', 'roadmap']

class FigureSerializer(serializers.ModelSerializer):
    items = SingleFigureSerializer(many=True,read_only=True)

    class Meta:
        model = Figure
        fields = ['placement_id', 'title_fi', 'title_sv', 'title_en', 'items']