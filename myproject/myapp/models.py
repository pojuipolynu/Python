from django.db import models

# Create your models here.

from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
    year = models.IntegerField()
    price = models.IntegerField(null=True)
