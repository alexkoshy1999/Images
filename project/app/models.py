from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):  
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  
        return self.caption

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)