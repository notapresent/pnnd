from django.contrib import admin

from .models import Section, Author, Article


class ArticleAdmin(admin.ModelAdmin):
    fields = ['section', 'author', 'title', 'intro', 'body', 'is_published',
              'pub_date', 'keywords']
    list_display = ('title', 'author', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title', 'intro','body']


admin.site.register(Section)
admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)
