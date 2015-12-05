# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_auto_20151105_0737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellers',
            name='picture',
        ),
        migrations.AddField(
            model_name='sellers',
            name='docfile',
            field=models.FileField(upload_to='documents/%Y/%m/%d', default=1),
            preserve_default=False,
        ),
    ]
