from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.TextField(max_length=20000000)
    likes = models.PositiveIntegerField(default=0)
