"""urlconf for the base application"""

from django.conf.urls.defaults import url, patterns, include


urlpatterns = patterns('djtut2.base.views',
    url(r'^$', 'home', name='home'),
)

urlpatterns += patterns('',
    url(r'^polls/', include('djtut2.polls.urls')),
)