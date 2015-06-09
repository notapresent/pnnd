# -*- coding: utf-8 -*-
from articles.models import Section


def global_vars(request):
    sections = Section.get_navlist()
    return {'sections': sections}
