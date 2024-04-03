from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    description = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photos = models.ManyToManyField(Photo, blank=True)