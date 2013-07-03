from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from sorl.thumbnail import ImageField


class Post(models.Model):
    title = models.CharField(_("Post title"), max_length=255)
    slug = models.SlugField(_("Post url"), unique=True)
    banner_content = models.TextField(_("Banner content"), blank=True, null=True)
    content = models.TextField(_("Post content"), blank=True, null=True)
    image = ImageField(upload_to="posts/top-images",
        verbose_name=_("Image")
    )
    show_on_main = models.BooleanField(default=True,
        verbose_name=_("Show on mainpage")
    )
    is_published = models.BooleanField(default=True,
        verbose_name=_("Is published")
    )
    url = models.CharField(max_length=255, blank=True, null=True,
        verbose_name=_("Redirect url")
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ("-created",)

    def __unicode__(self):
        return self.title

    def get_url(self):
        return self.url if self.url else \
            reverse('post-details', args=[self.slug])

    def show_url(self):
        if not self.url and not self.content:
            return False
        return True
