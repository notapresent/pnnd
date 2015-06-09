# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150609_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Заголовок'),
        ),
    ]
