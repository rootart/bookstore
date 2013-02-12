from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("Category name"), max_length=255)
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

    def __unicode__(self):
        return self.language


class Publisher(models.Model):
    name = models.CharField(_("Publisher name"), max_length=255)

    class Meta:
        verbose_name = _("Publisher")
        verbose_name_plural = _("Publishers")

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


class Product(models.Model):
    category = models.ForeignKey(Category,
        verbose_name=_("Category")
    )
    name = models.CharField(_("Product name"),
        max_length=255, blank=True, null=True
    )
    slug = models.SlugField(max_length=255, unique=True,
        verbose_name=_("Product slug")
    )
    description = models.CharField(_("Description"),
        max_length=255,
        blank=True, null=True
    )
    publisher = models.ForeignKey(Publisher, blank=True, null=True,
        verbose_name=_("Publisher")
    )
    publish_year = models.PositiveIntegerField(blank=True, null=True,
        verbose_name=_("Publishing year")
    )
    width = models.PositiveIntegerField(blank=True, null=True,
        verbose_name=_("Width"),
        help_text=_("in cm")
    )
    height = models.PositiveIntegerField(blank=True, null=True,
        verbose_name=_("Height"),
        help_text=_("in cm")
    )
    pages = models.PositiveIntegerField(blank=True, null=True,
        verbose_name=_("Number of pages")
    )
    binding = models.CharField(blank=True, null=True, max_length=255,
        verbose_name=_("Binding type")
    )
    language = models.ForeignKey(TextLanguage, blank=True, null=True,
        verbose_name=_("Text language")
    )
    available = models.BooleanField(verbose_name=_("Is available"))
    tags = models.ManyToManyField(Tags, blank=True, null=True,
        verbose_name=_("Tags")
    )

    price = models.PositiveIntegerField(blank=True, null=True,
        verbose_name=_("Price")
    )
    stock_price = models.PositiveIntegerField(blank=True, null=True,
        verbose_name=_("Stock price")
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("-modified",)

    def __unicode__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"))
    image = models.ImageField(upload_to="products/images",
        verbose_name=_("Image file")
    )
    caption = models.TextField(blank=True, null=True,
        verbose_name=_("Image caption")
    )

    class Meta:
        verbose_name = _("Product image")
        verbose_name_plural = _("Product images")

    def __unicode__(self):
        return self.products.name