from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=200)
    cuisine_type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    directions = models.CharField(max_length=200)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')

    def __str__(self):
        return self.name