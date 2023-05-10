from django.contrib import admin
from django.urls import path
from rest_framework import routers
from space_ms import views

router = routers.DefaultRouter()
router.register(r'spaces', views.SpaceViewSet, basename='space')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('space/', views.space, name='space'),
]

urlpatterns += router.urls