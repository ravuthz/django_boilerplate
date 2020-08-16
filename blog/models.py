from django.conf import settings
from django.db import models
from django.urls import reverse
from martor.models import MartorField
from taggit.managers import TaggableManager


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = MartorField()
    slug = models.SlugField(max_length=200, unique=True)
    tags = TaggableManager()
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='post_created')
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='post_updated')

    objects = PostQuerySet.as_manager()

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_details", kwargs={"slug": self.slug})
