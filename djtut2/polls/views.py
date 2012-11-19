from django.views.generic.list_detail import object_list, object_detail
from django.shortcuts import get_object_or_404, render_to_response

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p})
