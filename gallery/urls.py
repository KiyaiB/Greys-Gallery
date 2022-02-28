from .views import add_gallery_view

from django.urls import include, path

urlpatterns = [
    path('', add_gallery_view, name="index"),
]