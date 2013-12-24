from django.conf.urls import patterns, include, url

urlpatterns = patterns('app_xss_platform.views',
    url(r'^$', 'index', name='xss-index'),
    url(r'^u/(?P<uid>\d+)/i/', 'inject_payload', name="xss-payload"),
    url(r'^u/(?P<uid>\d+)/s/', 'store_xss_info', name="xss_store"),
    
)
