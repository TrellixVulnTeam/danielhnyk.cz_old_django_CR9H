from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.flatpages import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^sefik/', include(admin.site.urls)),
#    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('spirit.urls')),
)
