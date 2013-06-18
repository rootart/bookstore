from django.contrib import admin

from .models import Category, Publisher, Tags, TextLanguage,\
    Product, ProductImage, BindingType

from sorl.thumbnail.admin import AdminImageMixin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "slug")


class PublisherAdmin(admin.ModelAdmin):
    list_display = ("__unicode__",)


class TagsAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "slug")


class TextLanguageAdmin(admin.ModelAdmin):
    list_display = ("__unicode__",)


class ProductImageInline(AdminImageMixin, admin.TabularInline):
    model = ProductImage


class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("__unicode__", "category", "extra_category", "available_status", "homepage_position",\
    "catalogue_position", "category_position", "stock_price")
    list_filter = ("show_on_main", "category", "available_status", "publisher")
    prepopulated_fields = {'slug': ('author', 'name')}
    inlines = [ProductImageInline,]
    fields = (
        ('category', 'category_position'), ('extra_category', 'extra_category_position'),
        ('catalogue_position',),
        ('show_on_main', 'homepage_position'),
        'author', 'name', 'additional_name_info', 'catalogue_name', 'slug',
        ('short_description', 'description'),
        'publisher', 'publish_year', 'binding_type', 'pages',
        'width', 'height', 'units', 'language', 'available_status',
        'price', 'stock_price', 'main_cover_image', 'catalogue_image', 'is_active'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher, PublisherAdmin)
#admin.site.register(Tags, TagsAdmin)
admin.site.register(TextLanguage, TextLanguageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BindingType)
