from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

# Create your views here.

@login_required
def index(request):
    return render(request, "index.html")


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = '/index/'


class CustomLogoutView(LogoutView):
    next_page = 'login'