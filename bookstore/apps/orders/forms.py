from django import forms

from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    product = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Order
        exclude = ('uuid', 'was_contacted', 'was_delivered')

    def save(self, *args, **kwargs):
        from catalogue.models import Product
        order = super(OrderForm, self).save(*args, **kwargs)
        return order
        