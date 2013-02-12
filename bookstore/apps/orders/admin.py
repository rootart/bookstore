from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ("__unicode__",)
    inlines = [OrderItemInline,]
