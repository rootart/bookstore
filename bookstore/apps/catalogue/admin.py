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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(TextLanguage, TextLanguageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BindingType)
