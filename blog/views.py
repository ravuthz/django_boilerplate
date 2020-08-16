from django.shortcuts import render
from django.views import generic

from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.published()
    template_name = 'blog/index.html'
    paginate_by = 9


class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post.html"


class PostArchive(generic.ListView):
    queryset = Post.objects.all().order_by("-created_at")
    template_name = 'blog/index.html'
    paginate_by = 9


def list_tags(request, tag):
    object_list = Post.objects.filter(tags__name=tag)
    context = {"object_list": object_list, "tag": tag}
    return render(request, 'blog/index.html', context)
