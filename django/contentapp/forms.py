from django import forms
from .models import Page, Shortcut, SingleFigure
from ckeditor.widgets import CKEditorWidget

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['page_id', 'title_fi', 'title_sv', 'title_en', 'content_fi', 'content_sv', 'content_en']
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class ShortcutForm(forms.ModelForm):
    class Meta:
        model = Shortcut
        fields = ['placement_id', 'title_fi', 'title_sv', 'title_en', 'content_fi', 'content_sv', 'content_en', 'image', 'image_alt_fi', 'image_alt_sv', 'image_alt_en', 'link']
    def __init__(self, *args, **kwargs):
        super(ShortcutForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class SingleFigureForm(forms.ModelForm):
    class Meta:
        model = SingleFigure
        fields = ['figure', 'title_fi', 'title_sv', 'title_en', 'description_fi', 'description_sv', 'description_en', 'thumbnail', 'iframe_fi', 'iframe_sv', 'iframe_en',
        'source_fi', 'source_sv', 'source_en', 'info_fi', 'info_sv', 'info_en', 'roadmap']
    def __init__(self, *args, **kwargs):
        super(SingleFigureForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'