# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='navbar_order',
            field=models.IntegerField(null=True, verbose_name='Позиция в навигационной панели', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='article',
            name='intro',
            field=models.TextField(verbose_name='Вступление'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(verbose_name='Опубликован', default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='keywords',
            field=models.CharField(max_length=250, verbose_name='Ключевые слова', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Дата публикации', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='author',
            name='firstname',
            field=models.CharField(max_length=250, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='lastname',
            field=models.CharField(max_length=250, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
    ]
