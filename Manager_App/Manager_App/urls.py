"""
URL configuration for Manager_App project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Restaurant Admin"
admin.site.site_title = "Restaurant Management Portal"
admin.site.index_title = "Welcome to Restaurant Management Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login_ms.urls')),
    path('', include('staff_ms.urls')),
    path('', include('space_ms.urls')),
    path('', include('menu_ms.urls')),
    path('', include('dailyspecial_ms.urls')),
    path('', include('restaurant_acc_ms.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

