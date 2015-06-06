from django.contrib import admin

from .models import NewsItem


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'is_own')
    list_filter = ['pub_date', 'is_own']
    search_fields = ['title', 'body']

admin.site.register(NewsItem, NewsAdmin)
