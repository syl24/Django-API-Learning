# from music_controler.api.models import Room
from django.contrib import admin
from django.urls import path
from .views import CreateRoomView, RoomView

urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
]
