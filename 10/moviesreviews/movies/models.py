from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(max_length=1000)


class Review(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
