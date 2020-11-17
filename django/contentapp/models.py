from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ordered_model.models import OrderedModel, OrderedModelBase

class Lang(models.TextChoices):
    FI = 'fi', "Suomi"
    SV = 'sv', "Sverige"
    EN = 'en', "English"

class Page(models.Model):
    lang = models.CharField(
        max_length=2,
        choices=Lang.choices,
        default=Lang.FI
    )
    title_fi = models.CharField(max_length=200)
    title_sv = models.CharField(max_length=200, default='Enter title')
    title_en = models.CharField(max_length=200, default='Enter title')
    content_fi = RichTextUploadingField(blank=True)
    content_sv = RichTextUploadingField(blank=True)
    content_en = RichTextUploadingField(blank=True)
    placement_id = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title_fi

    def get_absolute_url(self):
        return reverse('page_edit', kwargs={'pk': self.pk})
        

class Shortcut(models.Model):
    lang = models.CharField(
        max_length=2,
        choices=Lang.choices,
        default=Lang.FI
    )
    title_fi = models.CharField(max_length=500)
    title_sv = models.CharField(max_length=500, default='Enter title')
    title_en = models.CharField(max_length=500, default='Enter title')
    content_fi = models.TextField(blank=True)
    content_sv = models.TextField(default='Enter content')
    content_en = models.TextField(default='Enter content')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    link = models.URLField(max_length=500, blank=True)
    placement_id = models.IntegerField()

    class Meta:
        ordering = ['placement_id']

    def __str__(self):
        return self.title_fi

    def get_absolute_url(self):
        return reverse('shortcut_edit', kwargs={'pk': self.pk})

class Figure(models.Model):
    lang = models.CharField(
        max_length=2,
        choices=Lang.choices,
        default=Lang.FI
    )
    placement_id = models.IntegerField()
    title_fi = models.CharField(max_length=500, default='Enter title')
    title_sv = models.CharField(max_length=500, default='Enter title')
    title_en = models.CharField(max_length=500, default='Enter title')

    def __str__(self):
        return self.title_fi

class SingleFigure(OrderedModelBase):
    figure = models.ForeignKey(Figure, related_name='items', on_delete=models.CASCADE)
    lang = models.CharField(
        max_length=2,
        choices=Lang.choices,
        default=Lang.FI
    )
    title_fi = models.CharField(max_length=500)
    title_sv = models.CharField(max_length=500, default='Enter title')
    title_en = models.CharField(max_length=500, default='Enter title')
    description_fi = RichTextUploadingField(blank=True)
    description_en = RichTextUploadingField(blank=True)
    description_sv = RichTextUploadingField(blank=True)
    thumbnail = models.ImageField(upload_to='images/figures/', null=True, blank=True)
    iframe_fi = models.CharField(max_length=500, blank=True)
    iframe_en = models.CharField(max_length=500, blank=True)
    iframe_sv = models.CharField(max_length=500, blank=True)
    link_id = models.CharField(max_length=4, blank=True)
    placement_id = models.PositiveIntegerField(editable=False, db_index=True)
    order_field_name = "placement_id"
    order_with_respect_to = 'figure'
    source_fi = models.CharField(max_length=500, blank=True)
    source_en = models.CharField(max_length=500, blank=True)
    source_sv = models.CharField(max_length=500, blank=True)
    info_fi = RichTextUploadingField(blank=True)
    info_en = RichTextUploadingField(blank=True)
    info_sv = RichTextUploadingField(blank=True)
    roadmap = models.BooleanField(default=False)

    class Meta:
        # unique_together = ['figure', 'placement_id']
        ordering = ['placement_id']

    def __str__(self):
        return '%d: %s' % (self.placement_id, self.title_fi)