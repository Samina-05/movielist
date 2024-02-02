from django.db import models

class Movie(models.Model):
    movie_name=models.CharField(max_length=100)
    release_date=models.DateField

    def __str__(self):
        return self.movie_name

# Create your models here.