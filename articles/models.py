import datetime

from django.db import models


class Section(models.Model):
    class Meta:
        verbose_name_plural = "Разделы"
        verbose_name = "Раздел"

    title = models.CharField('Название', max_length=250)
    slug = models.CharField(max_length=64)
    navbar_order = models.IntegerField('Позиция в навигационной панели',
                                       blank=True, null=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_navlist(cls):
        return cls.objects.order_by('navbar_order')


class Author(models.Model):
    class Meta:
        verbose_name_plural = "Авторы"
        verbose_name = "Автор"

    firstname = models.CharField('Имя', max_length=250)
    lastname = models.CharField('Фамилия', max_length=250)
    has_picture = models.BooleanField()

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)


class Article(models.Model):
    class Meta:
        verbose_name_plural = "Материалы"
        verbose_name = "Материал"

    section = models.ForeignKey(Section)
    author = models.ForeignKey(Author, null=True)
    pub_date = models.DateTimeField('Дата публикации',
                                    default=datetime.datetime.now)
    is_published = models.BooleanField('Опубликован',  default=True)
    title = models.CharField('Заголовок', max_length=250)
    intro = models.TextField('Вступление')
    body = models.TextField('Текст')
    has_picture = models.BooleanField()
    keywords = models.TextField('Ключевые слова', blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_latest(cls, section, n):
        filters = {'is_published': True}

        if section:
            filters['section'] = section.id

        return cls.objects.filter(**filters).order_by('-pub_date')[:n]

    @classmethod
    def last_in_section(cls, section, n=2):
        if isinstance(section, (str,bytes)):
            sec = Section.objects.filter(slug=section).first()
        else:
            sec = Section.objects.get(section)

        articles = cls.objects.filter(section=sec).order_by('-pub_date')[:n]
        return {
            'section': sec,
            'articles': articles
        }
