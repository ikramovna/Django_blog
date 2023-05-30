from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.EmailField()
    projects = models.IntegerField()
    image = models.ImageField(upload_to='media/users/')
