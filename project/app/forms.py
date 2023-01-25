from django import forms
from .models import Image


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'caption', 'tags')
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)