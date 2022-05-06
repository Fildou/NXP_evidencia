from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('scan/', views.scan, name='dashboard-scan'),
    path('borrowed/', views.borrowed, name='dashboard-borrowed'),
]
