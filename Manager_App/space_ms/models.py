from django.db import models
from django.contrib.auth.models import User


class Space(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='spaces/')
    num_tables = models.IntegerField(default=0)
    num_seats = models.IntegerField(default=0)
    parking_spaces = models.BooleanField(default=False)