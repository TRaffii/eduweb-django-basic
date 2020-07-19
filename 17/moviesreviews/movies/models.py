from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
