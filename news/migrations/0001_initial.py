# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('is_published', models.BooleanField()),
                ('is_own', models.BooleanField()),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('keywords', models.CharField(max_length=250)),
            ],
        ),
    ]
