import datetime
from functools import wraps
from functools import update_wrapper
from urllib import urlencode
from django.conf import settings
from django.contrib.admin import util as admin_util
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib import admin
from django.utils.html import strip_tags
from django.contrib import messages
from django.db.models import Q
from django.contrib.admin.util import label_for_field
from django.utils.translation import ugettext_lazy as _

from .models import Category, Publisher, Tags, TextLanguage,\
    Product, ProductImage, BindingType

from sorl.thumbnail.admin import AdminImageMixin


class AdjustableColumnsAdminMixin(object):

    change_list_template = 'admin/change_list_with_adjustable_fields.html'

    def get_list_display(self, request):
        """
        Return a sequence containing the fields to be displayed on the
        changelist.
        """

        info = self.admin_site.name, self.model._meta.app_label, self.model._meta.module_name
        return request.session.get(
            '%s_%s_%s_list_display' % info,
            getattr(self, 'default_list_display', self.list_display)
        )

    def get_urls(self):

        from django.conf.urls import url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)
        info = self.model._meta.app_label, self.model._meta.module_name

        urlpatterns = super(AdjustableColumnsAdminMixin, self).get_urls()

        return [
            url(r'^change_columns/$',
                wrap(self.change_list_display),
                name='%s_%s_change_list_display' % info
                )
            ] + urlpatterns

    def get_change_column_form(self):

        choices = [
            (field, (label_for_field(field, self.model, model_admin=self)).capitalize()) \
            for field in self.list_display
        ]

        class AdjustableColumnsForm(forms.Form):
            columns = forms.MultipleChoiceField(
                choices=choices,
                widget=FilteredSelectMultiple('columns', False)
            )

        return AdjustableColumnsForm

    def change_list_display(self, request):

        form = self.get_change_column_form()(request.POST or None, initial={
                'columns': self.get_list_display(request)
            }
        )
        if form.is_valid():
            info = self.admin_site.name, self.model._meta.app_label, self.model._meta.module_name
            request.session['%s_%s_%s_list_display' % info] = form.cleaned_data['columns']
        else:
            messages.error(request, _('Error changing columns'))
        return HttpResponseRedirect('../')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            'columns_form': self.get_change_column_form()(
                initial={'columns': self.get_list_display(request)}
            )
        })
        return super(AdjustableColumnsAdminMixin, self).changelist_view(request, extra_context)


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
    ordering = ('position',)


class CategoryProductGroupFilter(admin.SimpleListFilter):
    title = _('Category or Extra Category')
    parameter_name = 'ce'

    def lookups(self, request, model_admin):
        return Category.objects.values_list('id', 'name')

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        else:
            val = int(self.value())
            return queryset.filter(Q(category__id=val) | Q(extra_category__id=val))

class ProductAdmin(AdjustableColumnsAdminMixin, AdminImageMixin, admin.ModelAdmin):
    list_display = ("__unicode__", "category", "extra_category", "available_status", "homepage_position",\
    "catalogue_position", "category_position", "stock_price")
    list_filter = ("show_on_main", CategoryProductGroupFilter, "category", "available_status", "publisher")
    prepopulated_fields = {'slug': ('author', 'name')}
    inlines = [ProductImageInline,]
    fields = (
        ('category', 'category_position'), ('extra_category', 'extra_category_position'),
        ('catalogue_position',),
        ('show_on_main', 'homepage_position'),
        'author', 'name', 'additional_name_info', 'catalogue_name', 'slug',
        ('short_description', 'description_url', 'description'),
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
