from django.contrib import admin
from . models import personalInfo, Category, Location, Photo


# Register your models here.

admin.site.register(personalInfo)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Photo)