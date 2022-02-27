from django.db import models

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

def upload_gallery_image(instance, filename):
    return f"images/{instance.gallery.name}/gallery/{filename}"

class Image(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)
    image_name = models.CharField(max_length=200)
    image_description = models.CharField(max_length=500)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="images")