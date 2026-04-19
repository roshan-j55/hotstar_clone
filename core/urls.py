from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('video/<int:id>/', views.video_detail, name='video_detail'),
]