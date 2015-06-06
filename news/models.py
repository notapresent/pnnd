from django.db import models


class NewsItem(models.Model):
    pub_date = models.DateTimeField('date published')
    is_published = models.BooleanField()
    is_own = models.BooleanField()
    title = models.CharField(max_length=250)
    body = models.TextField()
    keywords = models.CharField(max_length=250)
