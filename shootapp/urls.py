from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.defaults import *
from mainapp.views import *
from django.conf.urls.defaults import *
admin.autodiscover()

# And include this URLpattern...
urlpatterns = patterns('',
    ('^$', index),
    (r'^submit/', submit),
    (r'^idea/(\d{1,2})/$', idea),
    (r'^admin/', include(admin.site.urls)),
)
