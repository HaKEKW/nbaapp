from django.urls import path

from nba_news.views import *

urlpatterns = [
    path('', PostView.as_view(), name='posts_url'),

]