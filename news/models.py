# -*- coding: utf-8 -*-
import datetime

from django.db import models


class NewsItem(models.Model):
    class Meta:
        verbose_name_plural = "Новости"
        verbose_name = "Новость"

    pub_date = models.DateTimeField('Дата публикации',
                                    default=datetime.datetime.now)
    is_published = models.BooleanField('Опубликована', default=True)
    is_own = models.BooleanField('Собственная', default=True)
    title = models.CharField('Заголовок', max_length=300)
    body = models.TextField('Текст')
    keywords = models.TextField('Ключевые слова', blank=True)

    def __str__(self):
        return self.title
