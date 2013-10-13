from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from sorl.thumbnail import ImageField


class Post(models.Model):
    pre_title_section = models.CharField(_("Pre title section"), max_length=255,
        blank=True, null=True
    )
    title = models.CharField(_("Post title"), max_length=255)
    author_section = models.CharField(_("Author section"), max_length=255,
        blank=True, null=True
    )
    post_author_section = models.CharField(_("Post author section"), max_length=255,
        blank=True, null=True
    )
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
