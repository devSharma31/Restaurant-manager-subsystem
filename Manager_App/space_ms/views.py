from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
import requests
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
from space_ms.models import Space
from .serializers import SpaceSerializer


@login_required
def index(request):
    return render(request, "index.html")


class SpaceViewSet(viewsets.ModelViewSet):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer


def space(request):
    spaces = Space.objects.all()
    context = {'space': spaces}
    return render(request, 'space.html', context)

from django.contrib.auth.views import LogoutView


class CustomLogoutView(LogoutView):
    next_page = 'login'
