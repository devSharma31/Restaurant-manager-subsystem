from django.contrib import admin
from django.urls import path
from rest_framework import routers
from restaurant_acc_ms import views
from .views import RestaurantViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('restaurant_info/', views.restaurant_info, name='restaurant_info'),
    path('restaurant_info/', RestaurantViewSet.as_view({'get': 'list'}), name='restaurant_info')
]

urlpatterns += router.urls