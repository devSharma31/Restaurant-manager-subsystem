from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
import requests
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
from dailyspecial_ms.models import DailySpecial
from .forms import DailySpecialForm
from .serializers import DailySpecialSerializer

@login_required
def index(request):
    return render(request, "index.html")
    

class DailySpecialViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = DailySpecial.objects.all()
        serializer = DailySpecialSerializer(queryset, many=True)
        return Response(serializer.data)


    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)


    def create(self, request):
        serializer = DailySpecialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = DailySpecial.objects.all()
        daily_special = get_object_or_404(queryset, pk=pk)
        serializer = DailySpecialSerializer(daily_special)
        return Response(serializer.data)

    def update(self, request, pk=None):
        daily_special = get_object_or_404(DailySpecial, pk=pk)
        serializer = DailySpecialSerializer(daily_special, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        daily_special = get_object_or_404(DailySpecial, pk=pk)
        daily_special.delete()
        return Response(status=204)


def update_daily_special(request, id):
    restaurant = get_object_or_404(Restaurant, pk=id)
    if request.method == 'POST':
        form = DailySpecialForm(request.POST)
        if form.is_valid():
            daily_special = form.save(commit=False)
            daily_special.restaurant = restaurant
            daily_special.save()
            return redirect('restaurant_info')
    else:
        form = DailySpecialForm()
        context = {
            'form': form,
            'restaurant': restaurant,
        }
    return render(request, 'update_daily_special.html', context)


from django.contrib.auth.views import LogoutView


class CustomLogoutView(LogoutView):
    next_page = 'login'
