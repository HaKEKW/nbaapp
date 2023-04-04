from django.urls import path

from .views import *


urlpatterns = [
    path('rooms/', rooms, name='index_url'),
    path('rooms/<int:pk>/', room, name='room_url'),

]