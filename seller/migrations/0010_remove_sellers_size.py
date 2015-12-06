# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0009_auto_20151205_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellers',
            name='size',
        ),
    ]
