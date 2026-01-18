from django import forms
from myapp.models import uploader


class ImageForm(forms.ModelForm):
    class Meta:
        model=uploader
        fields='__all__'
        labels = {'photo':''}