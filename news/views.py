from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views import generic

from .models import NewsItem


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        """Return the last 50 published news."""
        return NewsItem.objects.filter(is_published=True).order_by('-pub_date')[:50]


# def detail(request, ni_id):
#     ni = get_object_or_404(NewsItem, pk=ni_id)
#     if not ni.is_published:
#         raise Http404()
#     return render(request, 'news/detail.html', {'ni': ni})

class DetailView(generic.DetailView):
    model = NewsItem
    template_name = 'news/detail.html'

    def get_queryset(self):
        return NewsItem.objects.filter(is_published=True).all()
