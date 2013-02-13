from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(_("Post title"), max_length=255)
    slug = models.SlugField(_("Post url"), unique=True)
    content = models.TextField(_("Post content"))
    image = models.ImageField(upload_to="posts/top-images")
    show_on_main = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ("-created",)

    def __unicode__(self):
        return self.title
