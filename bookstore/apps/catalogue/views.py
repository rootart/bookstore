from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Product, Category


def homepage(request):
    products = Product.objects.filter(available=True)
    data = {
        'products': products,
    }
    return render(request, 'index.html', data)


def catalogue(request):
    data = {
        'products': Product.objects.active().all()
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
        product = Product.objects.active(slug=slug, category=category)
    except (Category.DoesNotExist, Product.DoesNotExist):
        raise Http404

    data = {
        'product': product,
        'category': category
    }
    return render(request, 'book-details.html', data)


def search(request):
    data = {}
    return render(request, 'search.html', data)