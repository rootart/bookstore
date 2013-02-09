from django.contrib import admin

from .models import Category, Publisher, Tags, TextLanguage,\
    Product, ProductImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("__unicode__",)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ("__unicode__",)


class TagsAdmin(admin.ModelAdmin):
    list_display = ("__unicode__",)


class TextLanguageAdmin(admin.ModelAdmin):
    list_display = ("__unicode__",)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ("__unicode__",)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline,]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(TextLanguage, TextLanguageAdmin)
admin.site.register(Product, ProductAdmin)
