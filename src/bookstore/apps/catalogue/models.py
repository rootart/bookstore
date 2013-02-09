from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("Category name"), max_length=255)
    description = models.TextField(blank=True, null=True)
    position = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ("-position",)

    def __unicode__(self):
        return self.name


class TextLanguage(models.Model):
    language = models.CharField(max_length=255)

    def __unicode__(self):
        return self.language


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __unicode__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(_("Product name"),
        max_length=255, blank=True, null=True
    )
    description = models.CharField(_("Description"),
        max_length=255,
        blank=True, null=True
    )
    publisher = models.ForeignKey(Publisher, blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    binding = models.CharField(blank=True, null=True, max_length=255)
    language = models.ForeignKey(TextLanguage, blank=True, null=True)
    available = models.BooleanField()
    tags = models.ManyToManyField(Tags, blank=True, null=True)

    price = models.PositiveIntegerField(blank=True, null=True)
    stock_price = models.PositiveIntegerField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("-modified",)

    def __unicode__(self):
        return self.name
