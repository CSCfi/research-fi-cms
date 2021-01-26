from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ordered_model.models import OrderedModel, OrderedModelBase


class Lang(models.TextChoices):
    FI = "fi", "Suomi"
    SV = "sv", "Sverige"
    EN = "en", "English"


class Locations(models.TextChoices):
    HOME = "/", "Etusivu"
    PUBLICATIONS = "/results/publications", "Julkaisut"
    PROJECTS = "/results/fundings", "Hankkeet"
    INFRASTRUCTURES = "/results/infrastructures", "Infrastruktuurit"
    ORGANIZATIONS = "/results/organizations", "Organisaatiot"
    NEWS = "/news", "Uutiset"
    SCIENCEINNOVATIONPOLICY = (
        "/science-innovation-policy/research-innovation-system",
        "Tutkimus- ja innovaatiojärjestelmä",
    )
    FIGURES = (
        "/science-innovation-policy/science-research-figures",
        "Lukuja tieteestä ja tutkimuksesta",
    )
    NONE = "javascript:void(0)", "Script"
    INFO = "/service-info", "Tietoa palvelusta"
    SITEMAP = "/sitemap", "Sivukartta"
    ACCESSIBILITY = "/accessibility", "Saavutettavuus"
    PRIVACY = "/privacy", "Tietosuoja"


class Page(models.Model):
    lang = models.CharField(max_length=2, choices=Lang.choices, default=Lang.FI)
    title_fi = models.CharField(max_length=200)
    title_sv = models.CharField(max_length=200, default="Enter title")
    title_en = models.CharField(max_length=200, default="Enter title")
    content_fi = RichTextUploadingField(blank=True)
    content_sv = RichTextUploadingField(blank=True)
    content_en = RichTextUploadingField(blank=True)
    page_id = models.CharField(max_length=64, blank=True)

    class Meta:
        ordering = ["page_id"]

    def __str__(self):
        return self.title_fi

    def get_absolute_url(self):
        return reverse("page_edit", kwargs={"pk": self.pk})


class Shortcut(models.Model):
    placement_id = models.IntegerField()
    lang = models.CharField(max_length=2, choices=Lang.choices, default=Lang.FI)
    link = models.CharField(
        max_length=500, choices=Locations.choices, default=Locations.HOME
    )
    title_fi = models.CharField(max_length=500)
    title_sv = models.CharField(max_length=500, default="Enter title")
    title_en = models.CharField(max_length=500, default="Enter title")
    content_fi = models.TextField(blank=True)
    content_sv = models.TextField(default="Enter content")
    content_en = models.TextField(default="Enter content")
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    image_alt_fi = models.CharField(max_length=500, default="", blank=True)
    image_alt_sv = models.CharField(max_length=500, default="", blank=True)
    image_alt_en = models.CharField(max_length=500, default="", blank=True)

    class Meta:
        ordering = ["placement_id"]

    def __str__(self):
        return self.title_fi

    def get_absolute_url(self):
        return reverse("shortcut_edit", kwargs={"pk": self.pk})


class Figure(models.Model):
    placement_id = models.IntegerField()
    lang = models.CharField(max_length=2, choices=Lang.choices, default=Lang.FI)
    title_fi = models.CharField(max_length=500, default="Enter title")
    title_sv = models.CharField(max_length=500, default="Enter title")
    title_en = models.CharField(max_length=500, default="Enter title")

    def __str__(self):
        return self.title_fi


class SingleFigure(OrderedModelBase):
    figure = models.ForeignKey(Figure, related_name="items", on_delete=models.CASCADE)
    placement_id = models.PositiveIntegerField(editable=True, db_index=True)
    order_field_name = "placement_id"
    order_with_respect_to = "figure"
    lang = models.CharField(max_length=2, choices=Lang.choices, default=Lang.FI)
    title_fi = models.CharField(max_length=500)
    title_sv = models.CharField(max_length=500, default="Enter title")
    title_en = models.CharField(max_length=500, default="Enter title")
    description_fi = RichTextUploadingField(blank=True)
    description_sv = RichTextUploadingField(blank=True)
    description_en = RichTextUploadingField(blank=True)
    thumbnail = models.ImageField(upload_to="images/figures/", null=True, blank=True)
    iframe_fi = models.CharField(max_length=500, blank=True)
    iframe_sv = models.CharField(max_length=500, blank=True)
    iframe_en = models.CharField(max_length=500, blank=True)
    source_fi = models.CharField(max_length=500, blank=True)
    source_sv = models.CharField(max_length=500, blank=True)
    source_en = models.CharField(max_length=500, blank=True)
    info_fi = RichTextUploadingField(blank=True)
    info_sv = RichTextUploadingField(blank=True)
    info_en = RichTextUploadingField(blank=True)
    roadmap = models.BooleanField(default=False)
    visual_file_fi = models.FileField(upload_to="visuals/", null=True, blank=True)
    visual_file_sv = models.FileField(upload_to="visuals/", null=True, blank=True)
    visual_file_en = models.FileField(upload_to="visuals/", null=True, blank=True)

    class Meta:
        ordering = ["figure", "placement_id"]

    def __str__(self):
        return "%d: %s" % (self.placement_id, self.title_fi)


class Sector(models.Model):
    placement_id = models.PositiveIntegerField(editable=True, db_index=True)
    lang = models.CharField(max_length=2, choices=Lang.choices, default=Lang.FI)
    name_fi = models.CharField(max_length=500, default="Enter sector name")
    name_sv = models.CharField(max_length=500, default="Enter sector name")
    name_en = models.CharField(max_length=500, default="Enter sector name")
    subtitle_fi = models.CharField(max_length=500, blank=True)
    subtitle_sv = models.CharField(max_length=500, blank=True)
    subtitle_en = models.CharField(max_length=500, blank=True)
    iframe_fi = models.CharField(max_length=500, blank=True)
    iframe_sv = models.CharField(max_length=500, blank=True)
    iframe_en = models.CharField(max_length=500, blank=True)
    description_fi = RichTextUploadingField(blank=True)
    description_sv = RichTextUploadingField(blank=True)
    description_en = RichTextUploadingField(blank=True)
    icon = models.CharField(max_length=500, default="Add icon code")

    class Meta:
        ordering = ["placement_id"]

    def __str__(self):
        return self.name_fi


class Organization(OrderedModelBase):
    sector = models.ForeignKey(
        Sector, related_name="organizations", on_delete=models.CASCADE
    )
    placement_id = models.PositiveIntegerField(editable=True, db_index=True)
    order_field_name = "placement_id"
    order_with_respect_to = "sector"
    lang = models.CharField(max_length=2, choices=Lang.choices, default=Lang.FI)
    name_fi = models.CharField(max_length=500, default="Enter organization name")
    name_sv = models.CharField(max_length=500, default="Enter organization name")
    name_en = models.CharField(max_length=500, default="Enter organization name")
    link = models.CharField(max_length=500, default="Enter link target")

    class Meta:
        ordering = ["sector", "placement_id"]

    def __str__(self):
        return "%d: %s" % (self.placement_id, self.name_fi)


class ExternalLinksParent(models.Model):
    placement_id = models.PositiveIntegerField(editable=True, db_index=True)
    lang = models.CharField(max_length=2, choices=Lang.choices, default=Lang.FI)
    title_fi = models.CharField(max_length=500, default="Enter title")
    title_sv = models.CharField(max_length=500, default="Enter title")
    title_en = models.CharField(max_length=500, default="Enter title")

    class Meta:
        ordering = ["placement_id"]

    def __str__(self):
        return self.title_fi


class ExternalLink(OrderedModelBase):
    parent = models.ForeignKey(
        ExternalLinksParent, related_name="items", on_delete=models.CASCADE
    )
    placement_id = models.PositiveIntegerField(editable=True, db_index=True)
    order_field_name = "placement_id"
    order_with_respect_to = "parent"
    lang = models.CharField(max_length=2, choices=Lang.choices, default=Lang.FI)
    label_fi = models.CharField(max_length=500, default="Enter link label")
    label_sv = models.CharField(max_length=500, default="Enter link label")
    label_en = models.CharField(max_length=500, default="Enter link label")
    content_fi = models.CharField(max_length=1000, default="Enter content")
    content_sv = models.CharField(max_length=1000, default="Enter content")
    content_en = models.CharField(max_length=1000, default="Enter content")
    url = models.URLField(max_length=500, help_text="Enter link target")

    class Meta:
        ordering = ["parent", "placement_id"]

    def __str__(self):
        return "%d: %s" % (self.placement_id, self.label_fi)
