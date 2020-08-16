from django.urls import path

from . import feed
from .views import PostArchive, PostList, PostDetail, list_tags

urlpatterns = [
    path('', PostList.as_view(), name="post_list"),
    path('<slug:slug>', PostDetail.as_view(), name="post_details"),
    path('feed/', feed.LatestPosts(), name="post_feed"),
    path('tags/<slug:tag>', list_tags, name="post_tags"),
    path('archives/', PostArchive.as_view(), name="post_archives"),
    # path('archives/', ListView.as_view(
    #     queryset=Post.objects.all().order_by("-created"),
    #     template_name="blog/index.html"
    # ), name="post_archives"),
]
