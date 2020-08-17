from django import forms
from shortcuts.models import Shortcut
from ckeditor.widgets import CKEditorWidget

class ShortcutForm(forms.ModelForm):
    class Meta:
        model = Shortcut
        fields = ['title_fi', 'title_sv', 'title_en', 'content_fi', 'content_sv', 'content_en', 'image', 'link']
    def __init__(self, *args, **kwargs):
        super(ShortcutForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'