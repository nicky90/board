from django.conf.urls import patterns, url

import machines 

urlpatterns = patterns('machines.views',
    url(r'^$', 'index', name='index'),
    url(r'^accounts/register/$', 'register', name='register'),
    url(r'^profile/(?P<user>\w+)/$', 'profile', name='profile'),
    url(r'^release/(?P<machine>\w+)/$', 'release', name='release'),
    url(r'^applyfor/(?P<machine>\w+)/$', 'applyfor', name='applyfor'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^accounts/login/$', 'login', name='login'),
    url(r'^accounts/logout/$', 'logout', name='logout'),
)
