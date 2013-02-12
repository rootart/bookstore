from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "full_name", "email", "phone", "was_contacted", "was_delivered")
    list_filter = ("was_contacted", "was_delivered", "created", "modified")
    inlines = [OrderItemInline,]

admin.site.register(Order, OrderAdmin)
