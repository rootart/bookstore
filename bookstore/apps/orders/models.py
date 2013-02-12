from django.db import models
from django.utils.translation import ugettext_lazy as _

from catalogue.models import Product


class Order(models.Model):
    uuid = models.CharField(max_length=10, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    was_contacted = models.BooleanField()
    was_delivered = models.BooleanField()

    class Meta:
        verbose_name = _("Order")
        verbose_name = _("Orders")
        ordering = ("-created",)


class OrderItem(models.Model):
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = _("Ordering item")
        verbose_name_plural = _("Ordering items")

    def __unicode__(self):
        return "%s - %s" % (self.product.name, self.order.uuid)
