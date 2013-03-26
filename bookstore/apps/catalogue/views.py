# -*- coding: utf-8 -*-
import json

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings

from .models import Product, Category
from news.models import Post
from orders.forms import OrderForm


def homepage(request):
    products = Product.objects.filter(available=True, show_on_main=True)
    posts = Post.objects.filter(
        is_published=True,
        show_on_main=True
        ).select_related('category')

    data = {
        'products': products,
        'posts': posts
    }

    return render(request, 'index.html', data)


def catalogue(request):
    categories = Category.objects.all()
    data = {
        'products': Product.objects.active().all(),
        'categories': categories
    }

    return render(request, 'catalogue.html', data)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.active().filter(category=category)
    data = {
        'category': category,
        'products': products
    }
    return render(request, 'catalogue.html', data)


def book_details(request, category_slug, slug):
    try:
        category = Category.objects.get(slug=category_slug)
        product = Product.objects.active().filter(slug=slug, category=category)[0]
    except (Category.DoesNotExist, Product.DoesNotExist, IndexError):
        raise Http404

    data = {
        'product': product,
        'category': category
    }
    return render(request, 'book-details.html', data)


ORDER_POPUP_MESSAGE = u"""
    Спасибо за размещение заказа. Наши сотрудники свяжутся с Вами в ближайшее время.
"""


@csrf_exempt
def book_order(request, category_slug, slug):
    from orders.models import OrderItem
    form = OrderForm(request.POST or None)
    try:
        category = Category.objects.get(slug=category_slug)
        product = Product.objects.active().filter(slug=slug, category=category)[0]
    except (Category.DoesNotExist, Product.DoesNotExist):
        raise Http404
    if request.method == "POST" and form.is_valid():
        order = form.save()
        order_item = OrderItem.objects.create(order=order, product=product)
        subject = u"[%s] Новый заказ - %s" % (order.id, product.name)
        message = u"""
            Имя: %s
            Телефон: %s
            E-Mail: %s
            Книга: %s
        """ % (
            order.full_name,
            order.phone, order.email,
            product.name
        )
        send_mail(subject, message, settings.DEFAULT_FROM,
            settings.ORDER_MANAGERS, fail_silently=False)

        return HttpResponse(json.dumps({'message': ORDER_POPUP_MESSAGE}),
            mimetype="application/json")

    data = {
        'form': form,
        'product': product,
        'category': category
    }
    return render(request, 'book-order.html', data)


def search(request):
    data = {}
    return render(request, 'search.html', data)


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    data = {
        'post': post
    }
    return render(request, 'post-details.html', data)