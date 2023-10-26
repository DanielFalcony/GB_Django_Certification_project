from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    cooking_steps = models.TextField(default='', blank=True)
    cooking_time = models.TimeField()
    img = models.ImageField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
