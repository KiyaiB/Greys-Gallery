from django.contrib import admin
from .models import Gallery, Category, Image

# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]