from django.contrib import admin

from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "is_active", "created", "modified")
    list_filters = ("is_active", "created")

admin.site.register(Subscription, SubscriptionAdmin)
