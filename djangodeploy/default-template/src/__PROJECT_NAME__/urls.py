from django.conf.urls.defaults import patterns, url, include, handler500, handler404
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include(admin.site.urls)),
    )
