from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
import requests
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
from menu_ms.models import Menu
from .serializers import MenuSerializer

@login_required
def index(request):
    return render(request, "index.html")


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


def menu(request):
    menus = Menu.objects.all()
    context = {'menus': menus}
    return render(request, 'menu.html', context)


from django.contrib.auth.views import LogoutView


class CustomLogoutView(LogoutView):
    next_page = 'login'