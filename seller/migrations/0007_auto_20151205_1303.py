# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0006_auto_20151205_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellers',
            name='docfile',
            field=models.FileField(upload_to='/project_images/'),
        ),
    ]
