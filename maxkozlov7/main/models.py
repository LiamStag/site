from django.db import models

# Create your models here.

class Works(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=true)
    video = models.FileField(upload_to="video/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=true)
    time_update = models.DateTimeField(auto_now=true)
    is_published = models.BooleanField(default=True)
