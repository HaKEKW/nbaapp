from django.shortcuts import render
from django.views.generic import ListView

from nba_news.models import Post


# Create your views here.

class PostView(ListView):
    model = Post
    template_name = 'nba_news/posts_list.html'
    context_object_name = 'posts'


