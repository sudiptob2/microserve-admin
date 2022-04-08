from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=20000)
    likes = models.PositiveIntegerField(default=0)
