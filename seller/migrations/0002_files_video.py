# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='video',
            field=models.TextField(default='hue'),
            preserve_default=False,
        ),
    ]
