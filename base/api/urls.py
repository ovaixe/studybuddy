from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('rooms', views.getRoomsOrCreateRoom),
    path('rooms/<str:pk>', views.getRoom),
    path('topics', views.getTopicsOrCreateTopic),
    path('messages', views.getMessages),
]

