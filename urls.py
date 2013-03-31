from django.conf.urls import patterns, include, url
from django.views.generic import DetailView
from bautomate.models import TelldusDevice

urlpatterns = patterns('',
    url(r'^$', 'bautomate.views.index'),
    url(r'^device/(?P<device_id>\d+)/$', DetailView.as_view(
        model=TelldusDevice,
        template_name='bautomate/detail.html')),
    url(r'^device/(?P<device_id>\d+)/switch/$', 'bautomate.views.switch'),
)
