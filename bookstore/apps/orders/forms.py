# -*- coding: utf-8 -*-
from django import forms

from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    product = forms.CharField(widget=forms.HiddenInput(), required=False)
    full_name = forms.CharField(label="Ваше имя", required=False,
        widget=forms.TextInput(attrs={'data-required': 'false'})
    )
    email = forms.CharField(required=True, label="Ваш e-mail*",
        widget=forms.TextInput(attrs={
            'data-pattern': '^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$',
            'data-required': 'true'}
            )
    )
    phone = forms.CharField(required=True, label="Контактный телефон*",
        widget=forms.TextInput(attrs={'data-required': 'true'})
    )
    
    class Meta:
        model = Order
        exclude = ('uuid', 'was_contacted', 'was_delivered', 'address', 'comments')

    def save(self, *args, **kwargs):
        from catalogue.models import Product
        order = super(OrderForm, self).save(*args, **kwargs)
        return order
        