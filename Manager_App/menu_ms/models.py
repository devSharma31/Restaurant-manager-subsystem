from django.db import models
from django.contrib.auth.models import User
from restaurant_acc_ms.models import Restaurant

class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    nutrition_info = models.TextField()
    allergy_info = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

