# -*- coding: utf-8 -*-
from articles.models import Section, Article


def global_vars(request):
    sections = Section.get_navlist()
    rightcol_sections = ['analytics', 'trend', 'discussion', 'docs',
                         'politfiction']
    rc_articles = {s: Article.last_in_section(s) for s in rightcol_sections}
    return {'sections': sections, 'right_column_data': rc_articles}
