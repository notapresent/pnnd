# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='body',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='is_own',
            field=models.BooleanField(verbose_name='Собственная', default=True),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='is_published',
            field=models.BooleanField(verbose_name='Опубликована', default=True),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='keywords',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Дата публикации', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
    ]
