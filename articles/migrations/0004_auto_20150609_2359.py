# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150609_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='keywords',
            field=models.TextField(blank=True, verbose_name='Ключевые слова'),
        ),
    ]
