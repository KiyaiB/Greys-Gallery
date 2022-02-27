from django import forms
from .models import Gallery, Category, Gallery, Image

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('name',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)