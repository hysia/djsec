from django.conf.urls import patterns, include, url

urlpatterns = patterns('app_tools.views',
    url(r'^$', 'tools_index', name='tools-index'),
   
)
