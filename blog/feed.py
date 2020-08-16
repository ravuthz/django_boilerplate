from django.contrib.syndication.views import Feed
from django.urls import reverse

from .models import Post


class LatestPosts(Feed):
    link = "/feed/"
    title = "Blog"
    description = "Latest Posts of Blog"

    def items(self):
        # return Post.objects.published()[:5]
        return Post.objects.published()

    def item_link(self, item):
        return reverse("post_details", kwargs={"slug": item.slug})
        # return u"/blog/%d" % item.id

    def item_title(self, item):
        return item.title
