from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',

url(r'^(\d*)$', views.index, name='index'),

url(r'^view/(?P<slug>[^\.]+)', 
    views.view_project,
    name='view_project'),

)
