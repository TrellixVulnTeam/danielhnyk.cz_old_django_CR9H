from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',

url(r'^(\d*)$', views.index, name='index'),

url(r'^view/(?P<slug>[^\.]+)', 
    views.view_post, 
    name='view_blog_post'),
    
url(r'^category/(?P<slug>[^\.]+)', 
    views.view_category, 
    name='view_blog_category'),
)
