from django.shortcuts import render

from .models import Product


def homepage(request):
    products = Product.objects.filter(available=True)
    data = {
        'products': products,
    }
    return render(request, 'index.html', data)


def catalogue(request):
    data = {}
    return render(request, 'catalogue.html', data)


def book_details(request, slug):
    data = {}
    return render(request, 'book-details.html', data)