import datetime

from django.db import models


class NewsItem(models.Model):
    pub_date = models.DateTimeField('Дата публикации',
                                    default=datetime.datetime.now)
    is_published = models.BooleanField('Опубликована', default=True)
    is_own = models.BooleanField('Собственная', default=True)
    title = models.CharField('Заголовок', max_length=250)
    body = models.TextField('Текст')
    keywords = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_latest(cls, n):
        return cls.objects.filter(is_published=True).order_by('-pub_date')[:n]
