from django.db import models
from django.urls import reverse

class Shortcut(models.Model):
    class Lang(models.TextChoices):
        FI = 'fi', "Suomi"
        SV = 'sv', "Sverige"
        EN = 'en', "English"

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
    image = models.ImageField(upload_to='images/', blank=True)
    link = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.title_fi

    def get_absolute_url(self):
        return reverse('shortcut_edit', kwargs={'pk': self.pk})