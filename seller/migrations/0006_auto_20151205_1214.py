# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_auto_20151205_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellers',
            name='docfile',
            field=models.FileField(upload_to='/%Y/%m/%d'),
        ),
    ]
