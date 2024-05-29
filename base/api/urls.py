from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/create', views.createRoom),
    path('rooms/<str:pk>/', views.getRoom),
    path('topics/', views.getTopics),
    path('topics/create', views.createTopic),
    path('messages/', views.getMessages),
]