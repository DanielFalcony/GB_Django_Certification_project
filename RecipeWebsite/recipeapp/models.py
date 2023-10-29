from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    cooking_steps = models.TextField(default='', blank=True)
    cooking_time = models.IntegerField()
    img = models.ImageField()
    # author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default='Author unknown')
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='Category unknown')
    add_time = models.DateField(auto_now_add=True)
