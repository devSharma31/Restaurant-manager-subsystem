from django.contrib import admin
from django.urls import path, include
from menu_ms import views
from .views import MenuViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'menus', views.MenuViewSet, basename='menu')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('menu/', views.menu, name='menu'),
    path('api/', include(router.urls)),
]

urlpatterns += router.urls