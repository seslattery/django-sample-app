from django.conf.urls.defaults import url, patterns
from django.views.generic import DetailView, ListView
from djtut2.polls.models import Poll

urlpatterns = patterns('',
    url(r'^$', 
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='recent_polls',
            template_name='polls/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html')),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        name='poll_results')
    # url(r'^(?P<pk>\d+)/vote/$',
    )