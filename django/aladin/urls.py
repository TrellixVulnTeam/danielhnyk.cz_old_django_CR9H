from django.conf.urls import patterns, url
from aladin import views

urlpatterns = patterns('',
    url(r'^$', views.get_urlofpic, name='get_urlofpic'),
    url(r'^result$', views.get_urlofpic, name='result'),
)
