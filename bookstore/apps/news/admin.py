from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from .models import Post


class PostAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("__unicode__", "slug", "is_published", "show_on_main",
        "created", "modified"
        )
    list_filter = ("is_published", "created", "modified")


admin.site.register(Post, PostAdmin)
