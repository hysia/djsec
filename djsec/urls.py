from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'djsec.views.home', name='home'),
    url(r'^dashboard/$', 'djsec.views.show_dashboard', name='show_dashboard'),
    url(r'^accounts/login/$', 'djsec.views.do_login', name='do_login'),
    url(r'^accounts/logout/$', 'djsec.views.do_logout', name='do_logout'),
    url(r'^accounts/profile/$', 'djsec.views.show_profile', name='show_profile'),
    url(r'^accounts/settings/$', 'djsec.views.show_settings', name='show_settings'),
    # Static files
    (r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    (r'^humans\.txt$', TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),
    (r'^crossdomain\.xml$', TemplateView.as_view(template_name='crossdomain.xml', content_type='text/xml')),
    # Installed Apps
    #url(r'^blog/', include('blog.urls')),
    url(r'^xss/', include('app_xss_platform.urls')),
    url(r'^tools/', include('app_tools.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
