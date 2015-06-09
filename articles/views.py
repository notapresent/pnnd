from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Article, Section


def latest(request, section_id=None):
    section = Section.get(section_id) if section_id else None
    articles = Article.get_latest(section_id, 25)
    context = {'articles': articles, 'section': section}
    return render(request, 'articles/latest.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if not article.is_published:
        raise Http404()
    return render(request, 'articles/detail.html', {'article': article})
