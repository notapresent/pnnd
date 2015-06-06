from django.contrib import admin

from .models import Section, Author, Article


# Register your models here.
admin.site.register(Section)
admin.site.register(Author)
admin.site.register(Article)
