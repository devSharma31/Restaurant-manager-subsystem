from django.contrib import admin
from django.urls import path
from dailyspecial_ms import views
from .views import DailySpecialViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'daily-specials', views.DailySpecialViewSet, basename='daily-special')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('update_daily_special/create/', views.DailySpecialViewSet.as_view({'post': 'create'}), name='update_daily_special_create'),
    path('update_daily_special/<int:pk>/update/', views.DailySpecialViewSet.as_view({'put': 'update'}), name='update_daily_special_update'),
    path('update_daily_special/<int:pk>/delete/', views.DailySpecialViewSet.as_view({'delete': 'destroy'}), name='update_daily_special_delete'),
    # Updated URL pattern for update_daily_special detail view
    path('update_daily_special/<int:pk>/', views.DailySpecialViewSet.as_view({'get': 'retrieve'}), name='update_daily_special'),
]

urlpatterns += router.urls
