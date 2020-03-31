from django.db import models


# Create your models here.

class Song(models.Model):

    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)


    def __str__(self):
        return self.title

