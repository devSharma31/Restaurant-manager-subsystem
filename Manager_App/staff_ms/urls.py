from django.contrib import admin
from django.urls import path
from staff_ms import views
from rest_framework import routers
from .views import StaffViewSet

router = routers.DefaultRouter()
router.register(r'staffs', views.StaffViewSet, basename='staff')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('staff/', views.staff, name='staff'),
]

urlpatterns += router.urls