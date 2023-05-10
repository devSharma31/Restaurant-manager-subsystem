from django.db import models
from django.contrib.auth.models import User
from restaurant_acc_ms.models import Restaurant

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=200)
    qualifications = models.TextField()
    experiences = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    

