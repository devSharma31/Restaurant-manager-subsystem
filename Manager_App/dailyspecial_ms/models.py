from django.db import models
from django.contrib.auth.models import User
from restaurant_acc_ms.models import Restaurant

# Create your models here.
class DailySpecial(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='daily_specials')
    menu = models.CharField(max_length=255)
    offers = models.TextField()
    discounts = models.TextField() 