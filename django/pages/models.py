from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Page(models.Model):
    class Lang(models.TextChoices):
        FI = 'fi', "Suomi"
        SV = 'sv', "Sverige"
        EN = 'en', "English"

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


    def __str__(self):
        return self.title_fi

    def get_absolute_url(self):
        return reverse('page_edit', kwargs={'pk': self.pk})