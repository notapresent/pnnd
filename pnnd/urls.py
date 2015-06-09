from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^news/', include('news.urls', namespace="news")),
    url(r'^articles/', include('articles.urls', namespace="articles")),
    url(r'^admin/', include(admin.site.urls)),
)
