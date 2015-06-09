import datetime

from django.db import models


class Section(models.Model):
    title = models.CharField('Название', max_length=250)
    slug = models.CharField(max_length=64)
    navbar_order = models.IntegerField('Позиция в навигационной панели',
                                       blank=True, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    firstname = models.CharField('Имя', max_length=250)
    lastname = models.CharField('Фамилия', max_length=250)
    has_picture = models.BooleanField()

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)


class Article(models.Model):
    section = models.ForeignKey(Section)
    author = models.ForeignKey(Author)
    pub_date = models.DateTimeField('Дата публикации',
                                    default=datetime.datetime.now)
    is_published = models.BooleanField('Опубликован',  default=True)
    title = models.CharField('Заголовок', max_length=250)
    intro = models.TextField('Вступление')
    body = models.TextField('Текст')
    has_picture = models.BooleanField()
    keywords = models.CharField('Ключевые слова', max_length=250, blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_latest(cls, section_id, n):
        filters = { 'is_published': True }

        if section_id:
            filters['section'] = section_id

        return cls.objects.filter(**filters).order_by('-pub_date')[:n]
