from django.contrib import admin
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

# Register your models here.
admin.site.register(Page)
admin.site.register(Shortcut)
admin.site.register(Figure)
admin.site.register(SingleFigure)
admin.site.register(Sector)
admin.site.register(Organization)
admin.site.register(ExternalLinksParent)
admin.site.register(ExternalLink)
