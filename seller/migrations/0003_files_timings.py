# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_files_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='timings',
            field=models.TextField(default='0900-1800'),
            preserve_default=False,
        ),
    ]
