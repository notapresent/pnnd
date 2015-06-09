# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150609_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='keywords',
            field=models.TextField(verbose_name='Ключевые слова', blank=True),
        ),
    ]
