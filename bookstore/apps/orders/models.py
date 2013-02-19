import random

from django.db import models
from django.utils.translation import ugettext_lazy as _

from catalogue.models import Product

NUMBERS = "0123456789"


def gen_uuid(range=5):
    return ''.join([random.choice(NUMBERS) for i in xrange(range)])

class Order(models.Model):
    uuid = models.CharField(max_length=10, unique=True,
        verbose_name=_("Order unique id")
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=255, blank=True, null=True,
        verbose_name=_("Full name")
    )
    email = models.EmailField(blank=True, null=True,
        verbose_name=_("Email")
    )
    phone = models.CharField(max_length=255, blank=True, null=True,
        verbose_name=_("Phone")
    )
    address = models.TextField(blank=True, null=True,
        verbose_name=_("Address")
    )
    comments = models.TextField(blank=True, null=True,
        verbose_name=_("Additional comments")
    )
    was_contacted = models.BooleanField(verbose_name=_("Was contacted"))
    was_delivered = models.BooleanField(verbose_name=_("Was delivered"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ("-created",)

    def __unicode__(self):
        return self.uuid

    def save(self, *args, **kwargs):
        if not self.uuid:
            uuid = gen_uuid()
            self.uuid = uuid
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"))
    order = models.ForeignKey(Order, verbose_name=_("Order"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantity"))

    class Meta:
        verbose_name = _("Ordering item")
        verbose_name_plural = _("Ordering items")

    def __unicode__(self):
        return "%s - %s" % (self.product.name, self.order.uuid)
