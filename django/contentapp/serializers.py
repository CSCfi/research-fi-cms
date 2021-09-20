from rest_framework import serializers

from .models import (
    Page,
    Shortcut,
    Figure,
    SingleFigure,
    Sector,
    Organization,
    ExternalLinksParent,
    ExternalLink,
)


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = (
            "page_id",
            "title_fi",
            "title_sv",
            "title_en",
            "content_fi",
            "content_sv",
            "content_en",
        )


class ShortcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortcut
        fields = [
            "placement_id",
            "title_fi",
            "title_sv",
            "title_en",
            "content_fi",
            "content_sv",
            "content_en",
            "image",
            "image_alt_fi",
            "image_alt_sv",
            "image_alt_en",
            "link",
        ]


class SingleFigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleFigure
        fields = [
            "placement_id",
            "title_fi",
            "title_sv",
            "title_en",
            "description_fi",
            "description_sv",
            "description_en",
            "thumbnail",
            "iframe_fi",
            "iframe_sv",
            "iframe_en",
            "source_fi",
            "source_sv",
            "source_en",
            "info_fi",
            "info_sv",
            "info_en",
            "roadmap",
            "visual_file_fi",
            "visual_file_sv",
            "visual_file_en",
            "visual_update_date_fi",
            "visual_update_date_sv",
            "visual_update_date_en",
        ]


class FigureSerializer(serializers.ModelSerializer):
    items = SingleFigureSerializer(many=True, read_only=True)

    class Meta:
        model = Figure
        fields = ["placement_id", "title_fi", "title_sv", "title_en", "items"]


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            "placement_id",
            "name_fi",
            "name_sv",
            "name_en",
            "link",
            "iframe_fi",
            "iframe_sv",
            "iframe_en",
        ]


class SectorSerializer(serializers.ModelSerializer):
    organizations = OrganizationSerializer(many=True, read_only=True)

    class Meta:
        model = Sector
        fields = [
            "placement_id",
            "name_fi",
            "name_sv",
            "name_en",
            "subtitle_fi",
            "subtitle_sv",
            "subtitle_en",
            "iframe_fi",
            "iframe_sv",
            "iframe_en",
            "description_fi",
            "description_sv",
            "description_en",
            "icon",
            "organizations",
        ]


class ExternalLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalLink
        fields = [
            "placement_id",
            "label_fi",
            "label_sv",
            "label_en",
            "content_fi",
            "content_sv",
            "content_en",
            "url_fi",
            "url_sv",
            "url_en",
        ]


class ExternalLinksParentSerializer(serializers.ModelSerializer):
    items = ExternalLinkSerializer(many=True, read_only=True)

    class Meta:
        model = ExternalLinksParent
        fields = ["placement_id", "title_fi", "title_sv", "title_en", "items"]
