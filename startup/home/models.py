from django.db import models

# Create your models here.
class StartupList(models.Model):
    title=models.CharField(max_length=255)
    content=models.CharField(max_length=2000)
    pic=models.ImageField(blank=True,upload_to="media/")
    location=models.CharField(max_length=255)
    technology=models.CharField(max_length=255)
    