# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail import ImageField


class Category(models.Model):
    name = models.CharField(_("Category name"), max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(_("Description"),
        blank=True, null=True
    )
    position = models.PositiveIntegerField(default=0,
        verbose_name=_("Position")
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ("-position",)

    def __unicode__(self):
        return self.name


class TextLanguage(models.Model):
    language = models.CharField(_("Language"), max_length=255)

    class Meta:
        verbose_name = _("Text language")
        verbose_name_plural = _("Text languages")
        ordering = ('language',)

    def __unicode__(self):
        return self.language


class Publisher(models.Model):
    name = models.CharField(_("Publisher name"), max_length=255)

    class Meta:
        verbose_name = _("Publisher")
        verbose_name_plural = _("Publishers")
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(_("Tag name"), max_length=255)
    slug = models.SlugField(max_length=255,
        verbose_name=_("Tag slug")
    )

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __unicode__(self):
        return self.name

class ProductManager(models.Manager):
    def active(self):
        return self.get_query_set().filter(is_active=True)


class Product(models.Model):

    AVAILABLE_STATUSES = (
        (0, _('Not available')),
        (1, _('Anticipating product')),
        (2, _('Is available'))
    )

    HARD_BINDING = u"твердый переплет"
    SOFT_BINDING = u"мягкая обложка"
    BINDING_TYPES = (
        ('hard', HARD_BINDING),
        ('soft', SOFT_BINDING)
    )
    category = models.ForeignKey(Category,
        verbose_name=_("Category")
    )
    homepage_position = models.PositiveIntegerField(default=0)
    category_position = models.PositiveIntegerField(default=0)
    catalogue_position = models.PositiveIntegerField(default=0)

    author = models.CharField(_("Author"), blank=True, null=True,
        max_length=255
    )
    name = models.CharField(_("Product name"),
        max_length=255, blank=True, null=True
    )
    additional_name_info = models.CharField(_("Additional product name info"),
        max_length=255, blank=True, null=True
    )
    catalogue_name = models.CharField(_("Catalogue product name"),
        max_length=255, blank=True, null=True
    )
    slug = models.SlugField(max_length=255, unique=True,
        verbose_name=_("Product slug")
    )
    short_description = models.TextField(_('Short description'),
        blank=True, null=True
    )
    description = models.TextField(_("Description"),
        blank=True, null=True
    )
    publisher = models.ForeignKey(Publisher, blank=True, null=True,
        verbose_name=_("Publisher")
    )
    publish_year = models.PositiveIntegerField(blank=True, null=True,
        verbose_name=_("Publishing year")
    )
    binding = models.CharField(blank=True, null=True, max_length=255,
        verbose_name=_("Binding type"),
        choices = BINDING_TYPES
    )
    pages = models.PositiveIntegerField(blank=True, null=True,
        verbose_name=_("Number of pages")
    )
    width = models.PositiveIntegerField(blank=True, null=True,
        verbose_name=_("Width")
    )
    height = models.PositiveIntegerField(blank=True, null=True,
        verbose_name=_("Height")
    )
    units = models.CharField(blank=True, null=True,
        max_length=255,
        verbose_name=_("Units"),
        help_text=_("Units for width and height")
    )
    language = models.ForeignKey(TextLanguage, blank=True, null=True,
        verbose_name=_("Text language")
    )
    available_status = models.PositiveIntegerField(
        choices = AVAILABLE_STATUSES,
        default=0
    )
    available = models.BooleanField(verbose_name=_("Is available"))
    anticipating = models.BooleanField(verbose_name=_("Anticipating product"))
    not_available = models.BooleanField(verbose_name=_("Not available"))
    tags = models.ManyToManyField(Tags, blank=True, null=True,
        verbose_name=_("Tags")
    )

    price = models.DecimalField(blank=True, null=True,
        verbose_name=_("Price"),
        max_digits=8, decimal_places=2
    )
    stock_price = models.DecimalField(blank=True, null=True,
        verbose_name=_("Stock price"),
        max_digits=8, decimal_places=2
    )

    created = models.DateTimeField(auto_now_add=True,
        verbose_name=_("Created date")
    )
    modified = models.DateTimeField(auto_now=True,
        verbose_name=_("Modified date")
    )
    is_active = models.BooleanField(default=True,
        verbose_name=_("Is active")
    )
    catalogue_image = ImageField(upload_to="catalogue/list-images",
        verbose_name=_("Catalogue image"),
        blank=True, null=True
    )
    main_cover_image = ImageField(upload_to="category/covers",
        verbose_name=_("Main cover image"),
        blank=True, null=True
    )
    show_on_main = models.BooleanField(default=False)

    objects = ProductManager()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("-modified",)

    def __unicode__(self):
        return self.name or self.author


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"))
    image = ImageField(upload_to="products/images",
        verbose_name=_("Image file")
    )
    caption = models.TextField(blank=True, null=True,
        verbose_name=_("Image caption")
    )

    class Meta:
        verbose_name = _("Product image")
        verbose_name_plural = _("Product images")

    def __unicode__(self):
        return self.product.name