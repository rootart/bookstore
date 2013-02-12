from django.conf.urls import patterns, url

urlpatterns = patterns('catalogue.views',
    url(r'^$', 'homepage', name='homepage'),
)