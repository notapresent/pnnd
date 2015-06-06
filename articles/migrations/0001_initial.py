# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('is_published', models.BooleanField()),
                ('title', models.CharField(max_length=250)),
                ('intro', models.TextField()),
                ('body', models.TextField()),
                ('has_picture', models.BooleanField()),
                ('keywords', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('has_picture', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='articles.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ForeignKey(to='articles.Section'),
        ),
    ]
