from django.contrib import admin

from nba_news.models import Post, Tag

# Register your models here.


admin.site.register(Post)
admin.site.register(Tag)