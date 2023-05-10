from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
import requests
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
from restaurant_acc_ms.models import Restaurant
from .serializers import RestaurantSerializer
from django.contrib.auth.views import LogoutView

@login_required
def index(request):
    return render(request, "index.html")

class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows restaurants to be viewed or edited.
    """
    queryset = Restaurant.objects.all().order_by('-id')
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

def restaurant_info(request):
    response = requests.get('http://127.0.0.1:8000/restaurants/')
    restaurants = response.json()
    json_data = response.content.decode('utf-8')
    return render(request, 'restaurant_info.html', {'restaurants': restaurants, 'json_data': json_data})


def update_restaurant_info(request):
    return render(request, "update_restaurant_info.html")
 


class CustomLogoutView(LogoutView):
    next_page = 'login'