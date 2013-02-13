from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "slug", "is_published", "show_on_main",
        "created", "modified"
        )
    list_filter = ("is_published", "created", "modified")


admin.site.register(Post, PostAdmin)
