from django import forms
from pages.models import Page
from ckeditor.widgets import CKEditorWidget

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title_fi', 'title_sv', 'title_en', 'content_fi', 'content_sv', 'content_en']
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'