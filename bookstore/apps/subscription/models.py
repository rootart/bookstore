from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()

    class Meta:
        verbose_name = _("Subscription")
        verbose_name_plural = _("Subscriptions")
        ordering = ("-modified",)

    def __unicode__(self):
        return self.email
