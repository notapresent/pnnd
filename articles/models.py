from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=64)


class Author(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    has_picture = models.BooleanField()


class Article(models.Model):
    section = models.ForeignKey(Section)
    author = models.ForeignKey(Author)
    pub_date = models.DateTimeField('date published')
    is_published = models.BooleanField()
    title = models.CharField(max_length=250)
    intro = models.TextField()
    body = models.TextField()
    has_picture = models.BooleanField()
    keywords = models.CharField(max_length=250)
