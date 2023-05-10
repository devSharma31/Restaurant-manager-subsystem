from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
import requests
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
from staff_ms.models import Staff
from .serializers import StaffSerializer

@login_required
def index(request):
    return render(request, "index.html")

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

def staff(request):
    staffs = Staff.objects.all()
    context = {'staff': staffs}
    return render(request, 'staff.html', context)


from django.contrib.auth.views import LogoutView


class CustomLogoutView(LogoutView):
    next_page = 'login'
