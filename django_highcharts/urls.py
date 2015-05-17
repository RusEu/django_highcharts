from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'highcharts.views.index', name='index'),
    url(r'^ip$', 'highcharts.views.ip_address_from_request', name='ip'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
