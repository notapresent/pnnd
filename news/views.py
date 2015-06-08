from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import NewsItem

from django.http import HttpResponse


def latest(request):
    latest_news = NewsItem.get_latest(50)
    context = {'latest_news_list': latest_news}
    return render(request, 'news/latest.html', context)

def single(request, ni_id):
    ni = get_object_or_404(NewsItem, pk=ni_id)
    if not ni.is_published:
        raise Http404()
    return render(request, 'news/single.html', {'ni': ni})

