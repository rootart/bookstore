from django.conf.urls import patterns, url

urlpatterns = patterns('catalogue.views',
    url(r'^$', 'homepage', name='homepage'),
    url(r'^subscribe/$', 'subscribe_email', name='subscribe'),
    url(r'^catalogue/$', 'catalogue', name='catalogue'),
    url(r'^catalogue/tag/(?P<slug>[-\w]+)/$', 'catalogue_by_tag', name='catalogue-by-tag'),
    url(r'^catalogue/(?P<slug>[-\w]+)/$', 'category', name='category-details'),
    url(r'^catalogue/(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', 'book_details', name='book-details'),
    url(r'^catalogue/(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/order/$', 'book_order', name='book-order'),
)