from django.db import models


class Photo(models.Model):
    name = models.CharField(max_length=255, default="Default Name")
    image = models.ImageField(upload_to='photos/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photos = models.ManyToManyField(Photo, blank=True)