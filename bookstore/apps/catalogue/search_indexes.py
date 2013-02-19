import datetime
from haystack import indexes

from .models import Product, Category

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    description = indexes.DateTimeField(model_attr='description')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        return self.get_model().objects.active()