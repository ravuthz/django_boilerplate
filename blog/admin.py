from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget

from .models import Post


# from django_markdown.admin import MarkdownInlineAdmin
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "tag_list", "created_by", "created_at",)
    list_filter = ("publish", "tags")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    exclude = ("created_by", "updated_by")

    # fieldsets = (
    #     (None, {'fields': ('tags',)}),
    # )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
