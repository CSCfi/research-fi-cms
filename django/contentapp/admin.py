from django.contrib import admin
from .models import Page, Shortcut, Figure, SingleFigure

# Register your models here.
admin.site.register(Page)
admin.site.register(Shortcut)
admin.site.register(Figure)
admin.site.register(SingleFigure)
